from tkinter import *
import customtkinter
from tkinter import messagebox
# Import the ChatGPTBot class from bot.py
from bot import ChatGPTBot



# Define the class for the chat app
class App:
    # The initializer method defines the GUI of the application window
    def __init__(self):
        # Initialize variables for the bot, KEY and bot_message
        self.bot = None
        self.KEY = ''
        self.bot_message = ''

        # Initiate the App
        # Create a new window using the CTk class from the customtkinter module
        self.window = customtkinter.CTk()
        # Set the title of the window
        self.window.title('ChatGPT-3.5 Bot')
        # Set the size of the window
        self.window.geometry('750x620')
        # Set the window icon
        self.window.iconbitmap('./icons/chat.ico')
        # Set dark mode
        customtkinter.set_appearance_mode('dark')
        # Set default color theme
        customtkinter.set_default_color_theme('green')


        # Create a frame for the chat window and its attached scrollbar
        frame_chatwin = customtkinter.CTkFrame(self.window, fg_color = '#242424')  # fg_color: color inside frame
        frame_chatwin.pack(pady = 20)  # pady: padding on y axis

        # Create a chat window as a Text widget within the frame
        # Set the background color (i.e. bg), width, border width (i.e. bd), font color (i.e. fg), relief style, text wrapping (i.e. wrap), and selection background color
        self.chat_window = Text(frame_chatwin,
                                bg = '#343638',
                                width = 65,
                                bd = 1,
                                fg = '#d6d6d6',
                                relief = 'flat',
                                wrap = WORD,
                                selectbackground = '#1f538d')  # wrap = WORD: When moving to the next line, the entire word will be wrapped to the next line instead of being split in the middle
                                                               # selectbackground: Defines the background color of the text when it is selected
        self.chat_window.grid(row = 0, column = 0)

        # Create a vertical scroll bar for the chat window
        scrollbar_chatwin = customtkinter.CTkScrollbar(frame_chatwin, command = self.chat_window.yview, orientation = 'vertical')
        scrollbar_chatwin.grid(row = 0, column = 1, sticky = N+S+W)

        # Configure the chat window to use the scrollbar for vertical scrolling
        self.chat_window.configure(yscrollcommand = scrollbar_chatwin.set,
                                   font = ('Arial'))   # Set the font to Arial


        # Create an entry widget for the user to enter their message
        self.user_msg_entry = customtkinter.CTkEntry(self.window,
                                                     placeholder_text = "Type your message here and hit the 'Enter' key",
                                                     width = 530,
                                                     height = 50,
                                                     border_width = 1)
        self.user_msg_entry.pack(pady = 10)
        # Bind the activity of pressing the Enter key to the send_text_message() function
        self.user_msg_entry.bind('<Return>', self.send_text_message)


        # Create a frame for 3 buttons
        frame_buttons = customtkinter.CTkFrame(self.window, fg_color = '#242424')
        frame_buttons.pack(pady = 10)

        # 'Update API Key' button
        # Create a button to update the API key. When clicked, it calls the show_key_part() function
        update_key_button = customtkinter.CTkButton(frame_buttons,
                                                    text = 'Update API Key',
                                                    command = self.show_key_part)
        update_key_button.grid(row = 0, column = 0, padx = 25)

        # 'Listen To Message' button
        # Create a button to play the bot's message in audio. When clicked, it calls the play_bot_message() function
        listen_button = customtkinter.CTkButton(frame_buttons,
                                               text = 'Listen To Message',
                                               command = self.play_bot_message)
        listen_button.grid(row = 0, column = 1, padx = 35)

        # 'Clear History' button
        # Create a button to clear the chat history while NOT reinitializing the chatbot. When clicked, it calls the clear_history() function
        clear_button = customtkinter.CTkButton(frame_buttons,
                                               text = 'Clear History',
                                               command = self.clear_history)
        clear_button.grid(row = 0, column = 2, padx = 25)


        # Create a frame for API key part
        self.frame_key = customtkinter.CTkFrame(self.window, border_width = 1)
        # This frame will be shown or hidden by the update_key_button and save_button

        # Create an Entry widget for the user to enter their API key
        self.key_entry = customtkinter.CTkEntry(self.frame_key,
                                                placeholder_text = 'Enter you API key here',
                                                width = 350,
                                                height = 50,
                                                border_width = 1)
        self.key_entry.grid(row = 0, column = 0, padx = 20, pady = 20)

        # Create 'Save Key' button for saving the entered API key. When clicked, it calls the save_key() function
        save_key_button = customtkinter.CTkButton(self.frame_key,
                                                  text = 'Save Key',
                                                  command = self.save_key)
        save_key_button.grid(row = 0, column = 1, padx = 10)


        # Start the tkinter event loop, which keeps the application running and handles user interactions
        self.window.mainloop()


    # Event function that sends the user's message to the bot and display chat history inside the chat window
    def send_text_message(self, event):
        # If the API key is not provided
        if self.KEY == '':
            # Display an error message that reminds the user to enter their API key
            messagebox.showerror('API Key Not Provided', 'Please enter your API key to initiate your chat!')
        # If the API key is provided
        else:
            # Get the text message from the user_msg_entry
            user_message = self.user_msg_entry.get()
            # If user's message is entered
            if user_message != '':
                # Insert the user's message into the chat window
                self.chat_window.insert(END, 'You: ' + user_message + '\n')
                # Send the user's message to the bot for processing and retrieve the bot's response
                self.bot_message = self.bot.chatting(user_message)
                # Insert the bot's message into the chat window
                self.chat_window.insert(END, 'Bot: ' + self.bot_message + '\n')
        # Clear the user message entry
        self.user_msg_entry.delete(0, END)


    # Clear the chat history and reset bot_message
    def clear_history(self):
        # Reset bot_message to empty string
        self.bot_message = ''
        # Delete all messages in the chat window
        self.chat_window.delete(1.0, END)


    # Play the audio of the bot's message using the bot's text-to-speech functionality
    def play_bot_message(self):
        # If the API key is not provided
        if self.KEY == '':
            # Display an error message to enter a valid API key
            messagebox.showerror('API Key Not Provided', 'Please enter your API key to initiate your chat!')
        # If the API key is provided
        else:
            # If the bot's message is not empty
            if self.bot_message != '':
                # Play the audio of the bot's message
                self.bot.saying(self.bot_message)


    # Display the API key part of the application window
    def show_key_part(self):
        # Expand the application window vertically to display the API key part
        self.window.geometry('750x770')
        # Show the frame for the API key part
        self.frame_key.pack(pady = 30)


    # Save the entered API key and initialize the chatbot with the new key
    def save_key(self):
        # Get the API key value from the key_entry
        self.KEY = self.key_entry.get()
        # If the the API key is entered
        if self.KEY != '':
            # Restore the application window back to its original size
            self.window.geometry('750x620')
            # Hide the frame for API key part
            self.frame_key.pack_forget()
            # Display a confirmation dialog to inform the user about the consequences of updating the API key
            ToSave = messagebox.askyesno("Update API Key",
                                         """Updating the API key requires RESTARTING the ChatBot, which will clear the chat history. Are you sure you want to proceed?""")
            # If the user confirms to update the API key
            if ToSave:
                # Clear the chat history
                self.clear_history()
                # Insert a message into the chat window indicating that the API key is being updated
                self.chat_window.insert(END, "[Updating API Key...]\n")

                try:
                    # Instantiate the ChatBot with the new API key
                    self.bot = ChatGPTBot(self.KEY)
                    # Send a test message to the chatbot to ensure it is working
                    self.bot_message = self.bot.chatting('hello')
                    # If the chatbot is successfully loaded, display a success message in the chat window...
                    self.chat_window.insert(END, "[Chatbot loaded successfully. You may BEGIN your conversation now.]\n")
                    # ...and the bot's response to the test message
                    self.chat_window.insert(END, 'Bot: ' + self.bot_message + "\n")
                # If the chatbot is failed to initialize
                except Exception as e:
                    # Display an error message indicating the API key is invalid
                    messagebox.showerror('Invalid API Key', 'API Key Invalid. Please ensure that a valid API key has been entered.')
                    # Reinitialize the 3 variables
                    self.bot = None
                    self.KEY = ''
                    self.bot_message = ''
                    # Clear the key_entry
                    self.key_entry.delete(0, END)
                    # Insert an error message into the chat window indicating the specific error encountered
                    self.chat_window.insert(END, '[ERROR: Invalid API key provided]\n')



# Run the ChatBot App
ChatBotApp = App()
