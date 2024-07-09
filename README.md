# Auto Youtube Shorts Maker

🤖 Automatically generate YouTube shorts simply by running the script!

## Description
From creation to editing and voiceover too, this script automates it all for a YouTube short. No more tedious tasks or endless hours, this script has you covered! And the best part? It's absolutely free!

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [How it Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Built Using](#built-using)

## Installation

### Prerequisites
1. **OpenAI API Key -** Get it from the [Open AI Website](https://platform.openai.com/account/api-keys). It provides $18 of free credits by default and they are more than enough. **[OPTIONAL]**
2. **OpenAI -** `pip install openai`
3. **gTTS -** `pip install gtts`
4. **MoviePY -** `pip install moviepy`
5. **Dotenv -** `pip install python-dotenv`

### Installing
1. Download this repository as a zip file or clone it using git.
2. Open the folder.
3. Make sure the above-mentioned modules are installed: `pip install -r requirements.txt`
4. Add your OpenAI API key to the `.env.example` file (`OPENAI_API=<key>`) and rename it to `.env` **[OPTIONAL]**
5. Download both gameplay videos from [Google Drive](https://drive.google.com/drive/folders/1qToyKgKDLOPgoMj_EMhA6qusV4xCr4Sb?usp=sharing) (as they were too large to upload to GitHub)
6. Put both videos in a folder named "`gameplay`" in the directory with the `shorts.py` file.
7. Run the `shorts.py` Python file.

## Usage

To use this script:
1. Run the `shorts.py` Python file.
2. Enter the name of the video.
3. Let AI generate video content for you or enter it yourself.
   - ***NOTE : (Make sure you have added your OpenAI API key in the `.env` file if using AI to generate content)***
4. And that's it! Everything else will be handled automatically!
5. You can find your video in the `generated/` directory.

## Demo

[Click Here To See The Demo Video](https://github.com/Binary-Bytes/Auto-YouTube-Shorts-Maker/blob/master/demo/Demo.mp4)

- ***NOTE : This video is trimmed but it shouldn't take more than 1 minute to generate your video.***

## How it Works

### 1. Content
The script starts by taking the video name and asking if the user wants to generate content using AI (which can be edited later).

### 2. Text-to-Speech
After the content is generated/entered by the user, it generates Text-to-Speech and saves the file as `speech.mp3`.

### 3. Editing
The editing starts by selecting a gameplay, trimming a random part of it, and adding speech on top of it. Next, it resizes the video to a 9:16 aspect ratio and saves the final video.

## Contributing

Note that this script is very basic as of now and does not generate any graphics like images or even subtitles. These are some things that may be added in the future. If you want to contribute, you are free to do so. Feel free to fork and improve this repository.

Due to school, exams, and other real-life commitments, I don't get much time to work on this project. When I do, I would like to add the above-mentioned features. Maybe even a Reddit video maker, but I'm not sure yet.

## License

<sup>`Beep boop, boop beep. I am a script. If there are any issues, contact my [Creator](https://github.com/Binary-Bytes) - BedrockGranny#8331 or bedrockgranny on Discord.`</sup>

## Built Using

1. [OpenAI API](https://platform.openai.com/docs/api-reference) - For generating video content.
2. [gTTS](https://gtts.readthedocs.io/en/latest/) - For Text-to-Speech.
3. [MoviePY](https://zulko.github.io/moviepy/) - For video editing.
