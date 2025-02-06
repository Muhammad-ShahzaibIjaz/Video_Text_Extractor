import moviepy.editor as mp
from pytube import YouTube
import math
import assemblyai as aai
import os


def videoDownloader(path):
  try:
    yt = YouTube(path)
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(139)
    stream.download('', 'audio.mp4')
  except:
    print("Connection Error")




def split_mp4_audio_to_text(input_file, chunk_duration, output_filename="response.txt"):
    aai.settings.api_key = "your assembly-ai api key here..."

    output_filename = "extracted_audio.wav"
    mp.AudioFileClip(input_file).write_audiofile(output_filename)
    clip = mp.AudioFileClip(output_filename)

    # FIRSTLY, CALCULATE THE AUDIO DURATION AND THEN ACCORDING TO THEM CALCULATE TOTAL NUMBER OF CHUNKS
    total_duration = clip.duration
    num_chunks = math.ceil(total_duration / chunk_duration)

    with open("response.txt", "a", encoding="utf-8") as text_file:

        # SPLIT AUDIO INTO CHUNKS
        for i in range(num_chunks):
            start_time = i * chunk_duration
            end_time = min(total_duration, start_time + chunk_duration)
            chunk = clip.subclip(start_time, end_time)
            chunk_filename = f"chunk_{i+1}.wav"
            chunk.write_audiofile(chunk_filename)

            audio_url = chunk_filename
            # en for english, hi for hindi you can change according to your required language
            config = aai.TranscriptionConfig(language_code="en")  
            transcriber = aai.Transcriber(config=config)
            transcript = transcriber.transcribe(audio_url)

            if transcript.status == "completed":
                text = transcript.text
                text_file.write(text + "\n")
                print(f"Chunk {i+1} transcribed successfully.")
            else:
                print(f"Error transcribing chunk {i+1}: {transcript.error}")
            # DELETION OF THE TEMPORARY DIVIDE AUDIO CHUNK 
            try:
                os.remove(chunk_filename)
            except FileNotFoundError:
                print(f"Chunk {chunk_filename} not found for deletion.")

    clip.close()


input_file = "audio.mp4"
chunk_duration = 10
videoDownloader("https://youtu.be/-mgGnx1p3b8?feature=shared")
split_mp4_audio_to_text(input_file, chunk_duration)
print(f"Audio from {input_file} split, transcribed to your need language, and appended to response.")
