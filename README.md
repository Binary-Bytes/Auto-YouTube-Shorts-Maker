# 🎥 Auto YouTube Shorts Maker

## 🚀 Project Overview

Automatically generate engaging 30-second educational YouTube Shorts using AI-powered script generation, text-to-speech, and dynamic gameplay footage.

## ✨ Key Features

- 🤖 AI-Driven Content Generation
- 🎙️ Automatic Text-to-Speech
- 🎮 Dynamic Video Composition
- 📱 Optimized Vertical Video Format

## 🛠️ Prerequisites

- Python 3.8+
- FFmpeg
- Internet Connection

## 📦 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Ravsalt/Auto-YouTube-Shorts-Maker.git
cd Auto-YouTube-Shorts-Maker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Prepare Templates:
- Create `templates/` directory
- Add gameplay clips (`short_*.mp4`)
- Create `generated/` output directory

## 🎬 Workflow

### 1. Topic Input
- Enter educational topic
- AI generates concise 30-second script

### 2. Script Generation
- Transforms topic into engaging narrative
- Focuses on clarity and insight
- Creates natural educational content

### 3. Video Composition
- Randomly selects gameplay clip
- Synchronizes audio and video
- Resizes to vertical format

### 4. Output
- Saves video in `generated/`
- Filename based on input topic

## 🔧 Customization

- Modify `TEMPLATE_FOLDER` for clip sources
- Adjust `OUTPUT_FOLDER` for exports

## 🔮 Roadmap

- [ ] Multi-language support
- [ ] Custom voice options
- [ ] Enhanced clip selection
- [ ] YouTube upload automation

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 🐛 Troubleshooting

- Verify FFmpeg installation
- Check internet connectivity
- Validate gameplay clip formats



### 1. Topic Selection
- Prompt user to enter an educational topic
- Topic serves as the foundation for content generation

### 2. Intelligent Script Creation
- AI-powered script generation using Pollinations API
- Transforms topic into concise, engaging 30-second narrative
- Focuses on clear, informative content
- Handles fallback to manual script input if API fails

### 3. Multimedia Composition
- **Audio Generation**: 
  - Converts script to natural text-to-speech
  - Creates MP3 voiceover

- **Video Integration**:
  - Randomly selects gameplay clip from `templates/`
  - Synchronizes audio with full video clip
  - Resizes to 9:16 vertical format

### 4. Content Optimization
- Ensures video duration matches audio length
- Generates title based on input topic
- Saves final video in `generated/` directory


## Contributing

This script is a work in progress. Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.
Potential future enhancements:
*   Adding subtitles.
*   More sophisticated video editing options.
*   Support for different TTS voices or services.



## Built Using

1.  **Pollinations AI** - For text-to-speech and script generation assistance.
2.  **MoviePy** - For video editing.
3.  **Requests** - For making HTTP requests to the API.
