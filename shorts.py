import os
import re
import random
import urllib.parse
import requests
import unicodedata
import glob
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.crop as crop_vid


# -------------------------- CONFIGS --------------------------
TEMPLATE_FOLDER = "templates"
OUTPUT_FOLDER = "generated"
GAMEPLAY_PATTERN = os.path.join(TEMPLATE_FOLDER, "short_*.mp4")


# -------------------- CLEANUP FUNCTION --------------------
def clean_script(text):
    # Remove [directions]
    text = re.sub(r"\[.*?\]", "", text)
    # Remove 'Voiceover' / 'Narrator' / tone indicators
    text = re.sub(r"^\s*(Voiceover|Narrator)?\s*\(?.*?\)?:\s*", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"^\s*(Voiceover|Narrator)\s*[-:]?\s*", "", text, flags=re.IGNORECASE | re.MULTILINE)
    # Remove asterisks
    text = text.replace("*", "")
    # Normalize quotes and other characters
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Strip extra whitespace
    return ' '.join(text.strip().split())


# ------------------ TEXT TO SPEECH WITH SCRIPT GENERATION -------------------
def generate_short_title(topic):
    # Remove common words and keep it concise
    words = topic.split()
    # Keep first 2-3 words, remove stop words
    stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'with'}
    title_words = [word for word in words if word.lower() not in stop_words][:3]
    # Capitalize and join
    return '_'.join(word.capitalize() for word in title_words)[:30]

def synthesize_speech_post(topic, out_path):
    # Clean and prepare the topic
    cleaned_topic = clean_script(topic)

    prompt = (
    f"Create an engaging 30-second educational short about {topic}. "
    "Make it informative, concise, and captivating. Explain the topic in a way that grabs the viewer's attention, "
    "uses clear language, and provides valuable insights. The goal is to educate and entertain simultaneously."
    ) + cleaned_topic

    # Encode the text for the URL
    encoded_text = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{encoded_text}?model=openai-audio&voice=onyx"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Check if the response is an audio file
        if 'audio/mpeg' in response.headers.get('Content-Type', ''):
            with open(out_path, 'wb') as f:
                f.write(response.content)
            print(f"Audio saved successfully as {out_path}")
            
            # Try to extract script from response text
            script = clean_script(response.text.strip()) if response.text else "No script generated."
            return script
        else:
            print("Error: Expected audio response, received:")
            print(f"Content-Type: {response.headers.get('Content-Type')}")
            print(response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making TTS request: {e}")
        return None


# -------------- SELECT RANDOM GAMEPLAY ----------------
def get_random_gameplay_clip(duration_limit):
    gameplay_files = glob.glob(GAMEPLAY_PATTERN)
    if not gameplay_files:
        raise FileNotFoundError("No gameplay templates found in 'templates/'")
    selected = random.choice(gameplay_files)
    clip = VideoFileClip(selected)
    return clip


# -------------- RESIZE TO 9:16 FORMAT ----------------
def resize_to_9_16(clip):
    w, h = clip.size
    target_ratio = 1080 / 1920
    if w / h > target_ratio:
        new_width = int(h * target_ratio)
        return crop_vid.crop(clip, width=new_width, height=h, x_center=w / 2, y_center=h / 2)
    else:
        new_height = int(w / target_ratio)
        return crop_vid.crop(clip, width=w, height=new_height, x_center=w / 2, y_center=h / 2)


# --------------- COMBINE AUDIO & VIDEO ----------------
def combine_clips(video_clip, audio_path):
    audio = AudioFileClip(audio_path)
    
    # If video_clip is None, we need to handle longer audio by combining multiple gameplay clips
    if video_clip is None:
        # For longer audio, stitch together multiple gameplay clips
        total_duration = audio.duration
        combined_clips = []
        remaining_duration = total_duration
        
        while remaining_duration > 0:
            # Get a clip for each segment (up to 30s each)
            segment_duration = min(remaining_duration, 30.0)
            segment_clip = get_random_gameplay_clip(segment_duration)
            segment_clip = segment_clip.set_duration(segment_duration)
            combined_clips.append(segment_clip)
            remaining_duration -= segment_duration
        
        # Concatenate all clips
        from moviepy.editor import concatenate_videoclips
        video_clip = concatenate_videoclips(combined_clips)
    else:
        # If audio is longer than video, extend video to audio's duration
        if audio.duration > video_clip.duration:
            video_clip = video_clip.set_duration(audio.duration)

    # Set the final duration
    duration = min(audio.duration, video_clip.duration)
    
    trimmed_video = video_clip.subclip(0, duration)
    trimmed_audio = audio.subclip(0, duration)
    return trimmed_video.set_audio(trimmed_audio), duration


# ---------------------- MAIN ------------------------
if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    topic = input("🎯 Enter topic for your short: ").strip()
    print("Generating Video : ")
    # Create speech and generate script via Pollinations API
    speech_path = os.path.join(OUTPUT_FOLDER, "speech.mp3")
    script = synthesize_speech_post(topic, speech_path)

    if script is None:
        # Fallback to manual script input if API fails
        script = clean_script(input("✍️ Enter your script manually: ").strip())
        title = input("🎬 Enter video title: ").strip().replace(" ", "_")
    else:
        # Use the auto-generated title
        title = generate_short_title(topic)

    try:
        # Load speech to determine exact duration
        speech_audio = AudioFileClip(speech_path)
        
        # For audio <= 30 seconds, use original logic
        if speech_audio.duration <= 30.0:
            gameplay_clip = get_random_gameplay_clip(speech_audio.duration + 1.3)
        else:
            # For longer audio, just pass None as video_clip
            gameplay_clip = None
            print(f"\n⚠️ Audio duration: {speech_audio.duration:.1f}s - Will combine multiple gameplay clips")
        
        # Combine clips (function will handle long audio appropriately)
        final_clip, actual_duration = combine_clips(gameplay_clip, speech_path)
        final_clip = resize_to_9_16(final_clip)
        
        # Output
        output_file = os.path.join(OUTPUT_FOLDER, f"{title}.mp4")
        final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac',
                                   temp_audiofile='temp-audio.m4a', remove_temp=True)
        
        print(f"\n✅ DONE. Video saved as: {output_file}")
        print(f"   Final duration: {actual_duration:.1f} seconds")
    except Exception as e:
        print(f"💥 ERROR: {e}")
