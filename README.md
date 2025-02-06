# YouTube Video to Text Converter

This Python script allows you to download audio from a YouTube video, split it into chunks, and transcribe it into text using AssemblyAI's speech-to-text API. The transcribed text is saved in a file (`response.txt`) for further use.

## Features

- **YouTube Video Downloader**: Downloads audio from a YouTube video in MP4 format.
- **Audio Splitting**: Splits the downloaded audio into smaller chunks for easier processing.
- **Speech-to-Text Conversion**: Converts audio chunks into text using AssemblyAI's transcription API.
- **Language Support**: Supports multiple languages for transcription (e.g., English, Hindi).
- **Temporary File Cleanup**: Automatically deletes temporary audio chunk files after transcription.

## Prerequisites

Before using this script, ensure you have the following:

1. **Python 3.x** installed on your system.
2. **AssemblyAI API Key**: Sign up at [AssemblyAI](https://www.assemblyai.com/) to get your API key.
3. **Required Python Libraries**:
   - `moviepy`
   - `pytube`
   - `assemblyai`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Muhammad-ShahzaibIjaz/Video_Text_Extractor.git
   cd Video_Text_Extractor

2. Install the required Python libraries:
   ```bash 
   pip install moviepy pytube assemblyai

3. Replace the placeholder AssemblyAI API key in the script with your own:
   ```bash
   aai.settings.api_key = "your_assemblyai_api_key_here"

## Output
The transcribed text will be saved in ```response.txt``` in the same directory as the script.

## Note
  - Ensure you have a stable internet connection for downloading and transcribing audio.
  - The script is designed to handle temporary files efficiently, but you can modify it to retain intermediate files if needed.
  - AssemblyAI's free tier has usage limits. For large-scale transcription, consider upgrading to a paid plan.
