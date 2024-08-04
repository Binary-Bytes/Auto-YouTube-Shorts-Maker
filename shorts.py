# Import everything
from dotenv import load_dotenv  # To load environment variables from a .env file
import random  # To generate random numbers
import os  # For interacting with the operating system (e.g., file paths)
import openai  # OpenAI's API to interact with their models like GPT
from gtts import gTTS  # Google's Text-to-Speech library for generating speech from text
from moviepy.editor import *  # MoviePy library for video editing
import moviepy.video.fx.crop as crop_vid  # For cropping video clips in MoviePy

# Load environment variables from a .env file
load_dotenv()

# Ask for video information from the user
title = input("\nEnter the name of the video >  ")  # Get the title of the video from the user
option = input('Do you want AI to generate content? (yes/no) >  ')  # Ask if the user wants AI-generated content

if option == 'yes':
    # Generate content using OpenAI API
    theme = input("\nEnter the theme of the video >  ")  # Ask for the theme of the video

    ### MAKE .env FILE AND SAVE YOUR API KEY ###
    # Set the OpenAI API key from environment variables
    openai.api_key = os.environ["OPENAI_API"]
    
    # Request content generation from OpenAI's GPT-3.5-turbo-instruct engine
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Specify the model to use
        prompt=f"Act as an script writer who writes engaging and professional scripts for tiktok shorts. you never do a grammatical mistake and write very engaging scripts that touches the viewers' attention. At the beginning of the video you never forget to add a viral hook that will catch the viewers attention and will break the scroll. Your scripts are so loved by users that they subscribe and follow the channel. Don't mention any channel's name but at appropriate point tell the viewer to like the video and follow or subscribe the channel or account. (Remember tiktok shorts have max limit of 1 min). Now Generate content on - \"{theme}\"",
        # Custom prompt asking the AI to generate a TikTok short script based on the theme
        temperature=0.7,  # Controls the creativity of the response
        max_tokens=200,  # Limits the response length
        top_p=1,  # Nucleus sampling parameter; keeps the top 100% likely tokens
        frequency_penalty=0,  # No penalty for repeating words
        presence_penalty=0  # No penalty for new topics
    )
    
    # Print the generated content for user review
    print(response.choices[0].text)
    
    # Ask the user if the generated content is acceptable
    yes_no = input('\nIs this fine? (yes/no) >  ')
    if yes_no == 'yes':
        content = response.choices[0].text  # Use the AI-generated content
    else:
        content = input('\nEnter >  ')  # Manually enter the content if AI-generated content is not acceptable
else:
    content = input('\nEnter the content of the video >  ')  # Manually enter the content if AI generation is not chosen

# Create the directory for saving the generated files if it doesn't exist
if os.path.exists('generated') == False:
    os.mkdir('generated')

# Generate speech for the video using Google's Text-to-Speech
speech = gTTS(text=content, lang='en', tld='ca', slow=False)  # Convert the content text to speech
speech.save("generated/speech.mp3")  # Save the generated speech to a file

# Select a random gameplay video and a random starting point
gp = random.choice(["1", "2"])  # Randomly select between two gameplay videos
start_point = random.randint(1, 480)  # Randomly select a start point in the video (between 1 and 480 seconds)
audio_clip = AudioFileClip("generated/speech.mp3")  # Load the generated speech as an audio clip

# Check if the speech duration fits within TikTok's time limits
if (audio_clip.duration + 1.3 > 58):  # Check if the total duration exceeds 58 seconds
    print('\nSpeech too long!\n' + str(audio_clip.duration) + ' seconds\n' + str(audio_clip.duration + 1.3) + ' total')
    exit()  # Exit the script if the speech is too long

print('\n')

### VIDEO EDITING ###

# Trim a random part of Minecraft gameplay and overlay the generated audio
video_clip = VideoFileClip("gameplay/gameplay_" + gp + ".mp4").subclip(start_point, start_point + audio_clip.duration + 1.3)
# Load the video, and trim it to match the length of the audio clip plus 1.3 seconds
final_clip = video_clip.set_audio(audio_clip)  # Set the generated speech as the audio for the video

# Resize the video to a 9:16 aspect ratio (standard for TikTok videos)
w, h = final_clip.size  # Get the original width and height of the video
target_ratio = 1080 / 1920  # Target aspect ratio (9:16)
current_ratio = w / h  # Calculate the current aspect ratio of the video

if current_ratio > target_ratio:
    # If the video is wider than the desired aspect ratio, crop the width
    new_width = int(h * target_ratio)  # Calculate the new width that fits the target ratio
    x_center = w / 2  # Find the horizontal center of the video
    y_center = h / 2  # Find the vertical center of the video
    final_clip = crop_vid.crop(final_clip, width=new_width, height=h, x_center=x_center, y_center=y_center)
    # Crop the video to the new width, keeping the height unchanged
else:
    # If the video is taller than the desired aspect ratio, crop the height
    new_height = int(w / target_ratio)  # Calculate the new height that fits the target ratio
    x_center = w / 2  # Find the horizontal center of the video
    y_center = h / 2  # Find the vertical center of the video
    final_clip = crop_vid.crop(final_clip, width=w, height=new_height, x_center=x_center, y_center=y_center)
    # Crop the video to the new height, keeping the width unchanged

# Write the final video to a file
final_clip.write_videofile("generated/" + title + ".mp4", codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)
# Save the final video with specified codecs and remove temporary files
