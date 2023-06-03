import openai
import pyttsx3
import re
import glob

# Define the class for the chatbot
class ChatGPTBot:
    # The initializer method gets executed when a new ChatGPTBot object (i.e. bot) is created
    def __init__(self, api_key):
        # Set up the OpenAI API Key
        self.api_key = api_key
        openai.api_key = self.api_key
        # Initialize the message history for chat storing
        self.message_history = []
        # Remove all previously existing audio files
        for file in glob.glob('./*.wav'):
            os.remove(file)


    # The bot sends the user's message to GPT model and receives API response
    # Document and update the message history between the user and the bot
    def chatting(self,
                 user_message,
                 model = "gpt-3.5-turbo",
                 role = 'user'):
        # Assemble a request using the user's message and append it to message_history
        request = {"role": role, "content": user_message}
        self.message_history.append(request)

        # Create a chat completion object using OpenAI API
        completion = openai.ChatCompletion.create(
          model = model,
          messages = self.message_history
        )

        # Extract bot's message from the API response
        bot_message = completion['choices'][0]['message']['content']
        # Assemble a response using the bot's message and append it to the message_history
        response = {"role": 'assistant', "content": bot_message}
        self.message_history.append(response)

        return bot_message



    # Retrieve a Chinese voice from pyttsx3 engine
    def get_chinese_voice(self, engine: pyttsx3.engine.Engine):
        # Retrieve the list of available voices from the engine
        voices = engine.getProperty("voices")
        # Iterate over each voice in the voices list
        for voice in voices:
            # Check if the voice has languages attribute and if the first language is "zh-CN"
            if voice.languages and voice.languages[0] == "zh-CN":
                # Return the current voice as it is a Chinese voice
                return voice
            # Check if the voice's name contains "Chinese" or "Mandarin" (case-insensitive)
            if "Chinese" in voice.name or "Mandarin" in voice.name.title():
                # Return the current voice as it is considered a Chinese voice
                return voice
        # If no Chinese voice is found among the available voices, raise a RuntimeError
        raise RuntimeError(f"No Chinese voice found among {voices}")


    # Make the bot speak a message
    def saying(self, bot_message):
        # Initialize the text-to-speech engine
        tts_engine = pyttsx3.init()
        # Play bot's message in audio - in Chinese or English?
        threshold = 0.5
         # Get a list of English words from the the bot's message
        en_words = re.findall("[a-zA-Z\']+", bot_message)
        # Get a list of Chinese characters from the bot's message
        ch_words = re.findall("[\u4e00-\u9FFF]", bot_message)  # detect chinese characters: eg. [['当', '然', '可', '以']
        # Total number of both Chinese characters and English words
        total_len = len(en_words) + len(ch_words)
        if total_len > 0:
            # Calculate the proportion of Chinese words in the message
            prop_ch = len(ch_words) / total_len
            # If the proportion of Chinese words is above the threshold, use a Chinese voice
            if prop_ch > threshold:
                # Retrieve a Chinese voice from the pyttsx3 engine using the get_chinese_voice function
                chinese_voice = self.get_chinese_voice(tts_engine)
                # Set the voice property of the pyttsx3 engine to the Chinese voice
                tts_engine.setProperty("voice", chinese_voice.id)
        # Convert the bot's message from text to speech
        tts_engine.say(bot_message)
        # Wait for the engine to complete speaking the message
        tts_engine.runAndWait()
