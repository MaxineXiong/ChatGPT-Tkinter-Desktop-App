from openai import OpenAI
import pyttsx3
import re
import glob
from threading import Thread



class ChatGPTBot:
    """Define the class for the Chatbot
    """

    def __init__(self, api_key: str):
        """Initializer method that is executed when a new ChatGPTBot
        object (i.e. bot) is created.
        Args:
        - api_key (string): The OpenAI API key used to authenticate
        with the OpenAI service.
        """
        # Instantiate a client object using the api_key
        self.client = OpenAI(api_key=api_key)
        # Initialize the message history for chat storing
        self.message_history = []


    def respond(self, user_message: str, model: str = "gpt-3.5-turbo"):
        """Method to send the user's message to GPT model and receive
        API response. This method also documents and updates the message
        history between the user and the bot.
        Args:
        - user_message (string): The user's input message.
        - model (string): The GPT model to use. Default is 'gpt-3.5-turbo'.
        """
        # Assemble a request using the user's message and ...
        # ...append it to message_history
        request = {"role": "user", "content": user_message}
        self.message_history.append(request)

        # Create a chat completion object
        completion = self.client.chat.completions.create(
            model=model, messages=self.message_history
        )

        # Extract bot's message from the API response
        bot_message = completion.choices[0].message.content
        # Assemble a response using the bot's message and ...
        # ...append it to the message_history
        response = {"role": "assistant", "content": bot_message}
        self.message_history.append(response)

        return bot_message


    def get_chinese_voice(self, engine: pyttsx3.engine.Engine):
        """Method to retrieve a Chinese voice from pyttsx3 engine
        Args:
        - engine (pyttsx3.engine.Engine): The pyttsx3 engine instance
        for converting text message to speech.
        """
        # Retrieve the list of available voices from the engine
        voices = engine.getProperty("voices")
        # Iterate over each voice in the voices list
        for voice in voices:
            # Check if the voice has languages attribute and ...
            # ...if the first language is "zh-CN"
            if voice.languages and voice.languages[0] == "zh-CN":
                # Return the current voice as it is a Chinese voice
                return voice
            # Check if the voice's name contains "Chinese" or "Mandarin"
            if "Chinese" in voice.name or "Mandarin" in voice.name.title():
                # Return the current voice as it is considered a Chinese voice
                return voice
        # If no Chinese voice is found among the available voices, ...
        # ...raise a RuntimeError
        raise RuntimeError(f"No Chinese voice found among {voices}")


    def speak(self, bot_message: str):
        """Method to convert bot's text message into speech.
        Args:
        - bot_message (string): The bot's message to be spoken.
        """
        # Initialize the text-to-speech engine
        tts_engine = pyttsx3.init()
        # Play bot's message in audio - in Chinese or English?
        threshold = 0.5
        # Get a list of English words from the the bot's message
        en_words = re.findall("[a-zA-Z']+", bot_message)
        # Get a list of Chinese characters from the bot's message.
        # The detected chinese characters will be like ['当', '然', '可', '以']
        ch_words = re.findall(
            "[\u4e00-\u9FFF]", bot_message
        )
        # Total number of both Chinese characters and English words
        total_len = len(en_words) + len(ch_words)
        if total_len > 0:
            # Calculate the proportion of Chinese words in the message
            prop_ch = len(ch_words) / total_len
            # If the proportion of Chinese words is above the threshold, ...
            # ...use a Chinese voice
            if prop_ch > threshold:
                # Retrieve a Chinese voice from the pyttsx3 engine using ...
                # ...the get_chinese_voice function
                chinese_voice = self.get_chinese_voice(tts_engine)
                # Set the voice property of the pyttsx3 engine to the ...
                # ...Chinese voice
                tts_engine.setProperty("voice", chinese_voice.id)
        # Lower the rate of the speech
        rate = tts_engine.getProperty("rate")
        tts_engine.setProperty("rate", rate - 20)
        # Convert the bot's message from text to speech
        tts_engine.say(bot_message)
        # Wait for the engine to complete speaking the message
        tts_engine.runAndWait()
