import speech_recognition as sr
import ollama
import gtts
import os
from pydub import AudioSegment
from pydub.playback import play

class AIAssistant:
    def __init__(self):
        pass

    def live_audio_transcription(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        print("Adjusting for ambient noise...")

        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            # Set phrase_time_limit to 10 seconds
            audio = recognizer.listen(source, phrase_time_limit=10)
            print("Audio captured, processing...")

        try:
            transcript = recognizer.recognize_google(audio)
            print("Transcription: " + transcript)
            return transcript
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    def generate_ai_response(self, transcript):
        if not transcript:
            print("No transcript available to process.")
            return

        print("Generating AI response...")

        # Stream response from Ollama using the provided transcript
        ollama_stream = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": transcript}],
            stream=True
        )

        complete_response = ""  # To accumulate the full response

        for response in ollama_stream:
            message = response.get("message")
            if message:
                content = message.get("content", "")
                complete_response += content  # Append each part of the response
            else:
                print("Received response without 'message':", response)

        # Once done, print the complete response
        if complete_response:
            print("AI Response: " + complete_response)
            return complete_response
        return ""

    
    
    def text_to_speech(self, text, speed_factor=1):
        tts = gtts.gTTS(text)
        audio_file = "response.mp3"
        tts.save(audio_file)

        # Load the audio file and adjust speed
        audio = AudioSegment.from_mp3(audio_file)
        new_sample_rate = int(audio.frame_rate * speed_factor)
        adjusted_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
        adjusted_audio = adjusted_audio.set_frame_rate(audio.frame_rate)

        # Save the adjusted audio to a new file
        adjusted_file = "response_adjusted.mp3"
        adjusted_audio.export(adjusted_file, format="mp3")

        # Play the adjusted audio file
        adjusted_audio = AudioSegment.from_mp3(adjusted_file)
        play(adjusted_audio)
        
        # Clean up the audio files
        os.remove(audio_file)
        os.remove(adjusted_file)

    def run(self):
        while True:
            # Get live transcription
            transcribed_text = self.live_audio_transcription()

            # Check if the user wants to exit
            if transcribed_text and "exit" in transcribed_text.lower():
                print("Exiting...")
                break

            # Generate AI response
            response_text = self.generate_ai_response(transcribed_text)

            # Convert response to speech and play it
            
            if response_text:
                self.text_to_speech(response_text,speed_factor=1.2)
                
# Create an instance of AIAssistant
assistant = AIAssistant()

# Run the assistant
assistant.run()
