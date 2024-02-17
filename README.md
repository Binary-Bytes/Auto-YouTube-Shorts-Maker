# Auto Youtube-Shorts

🤖 Automatically generate YouTube shorts simply by running the script!

## 📝 Table of Contents

1. [About](#about)
2. [Demo](#demo)
3. [How it works](#working)
4. [Getting Started](#getting_started)
5. [Usage](#usage)
6. [Built Using](#built_using)
7. [Note](#note)

<h2 id="about">🧐 About</h2>

From creation to editing and voiceover too for a YouTube short, this script automates it all. No more tedious tasks, endless hours, this script has you covered!

Absolutely free!

<h2 id="demo">🎥 Demo</h2>

![Working](https://user-images.githubusercontent.com/88529771/236298905-5abe9905-f6ef-4cfb-859e-2c663ae2025a.mp4)

- ***NOTE : This video is trimmed but it shouldn't take more than 1 minute to generate your video.***

<h2 id="working">💭 How it works</h2>

<h4>#1 Content</h4>
The script starts by taking the video name and asking if the user wants to generate content using AI (which can be edited later).

<h4>#2 Text-to-Speech</h4>
After the content is generated / entered by the user, it generates Text-to-Speech and saves the file as `speech.mp3`.

<h4>#3 Editing</h4>
The editing starts by selecting a gameplay, trimming a random part of it and adding speech on top of it. Next, it resizes the video to 9:16 aspect ratio and saves the final video.

<h2 id="getting_started">🏁 Getting Started</h2>

Follow the instructions given below to get this script up and running on your device.

<h4>Prerequisites</h4>

1. **OpenAI API Key -** Get it from the [Open AI Website](https://platform.openai.com/account/api-keys). It provides $18 of free credits by default and they are more than enough. **[OPTIONAL]**
2. **OpenAI -** `pip install openai`
3. **gTTS -** `pip install gtts`
4. **MoviePY -** `pip install moviepy`
5. **Dotenv -** `pip install python-dotenv`
6. **FFmpeg -** `brew install ffmpeg`

<h4>Installing</h4>

1. Download this repository as zip file / using git.
2. Open the folder.
3. Make sure the above mentioned modules are installed. (`pip install -r requirements.txt`)
4. Add your OpenAI API key to `.env.example` file (`OPENAI_API=<key>`) and rename it to just `.env` **[OPTIONAL]**
5. Now, download both the gameplay videos from [Google Drive](https://drive.google.com/drive/folders/1qToyKgKDLOPgoMj_EMhA6qusV4xCr4Sb?usp=sharing) (as they were too large to upload to Github)
6. Put both the videos in a folder named "`gameplay`" in the directory with `shorts.py` file.
7. Run the `shorts.py` python file.

<h2 id="usage">🎈 Usage</h2>

To use this script,

1. Run the `shorts.py` python file.
2. Enter the name of the video.
3. Let AI generate video content for you / enter it yourself.

- ***NOTE : (Make sure you have added your OpenAI API key in `.env` file if using AI to generate content)***

4. And that's it! Everything else will be handled automatically!
5. You can find your video in `generated/` directory.

---

`<sup>`Beep boop, boop beep. I am a script. If there are any issues, contact my [Creator](https://github.com/Binary-Bytes) - BedrockGranny#8331 `and/or` bedrockgranny on Discord `</sup>`

<h2 id="built_using">⛏️ Built Using</h2>

1. [OpenAI API](https://platform.openai.com/docs/api-reference) - For generating video content.
2. [gTTS](https://gtts.readthedocs.io/en/latest/) - For Text-to-Speech.
3. [MoviePY](https://zulko.github.io/moviepy/) - For video editing.

<h2 id="note">🗒️ Note</h2>

Note that this script is very basic as of now and does not generate any graphics like images or even subtitles. These are some things that I **MAY** add in the future. If you want to contribute, you are free to do so and you may even fork and improve this repository.

Due to school, exams and irl stuff I don't get much time to work on this project. When I do, I would like to add the above mentioned features. Maybe even a REDDIT video maker but not sure yet.
