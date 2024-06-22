from tkinter import *
import customtkinter
from tkinter import messagebox

# Import the ChatGPTBot class from bot.py
from bot import ChatGPTBot
from datetime import datetime



class TkinterApp:
    """Define the class for the chat app
    """

    def __init__(self):
        """Initializer method to define the GUI of the application
        window
        """
        # Initialize variables for the bot, KEY, MODEl and bot_message
        self.bot = None
        self.KEY = ""
        self.MODEL = ""
        self.bot_message = ""
        self.key_part_displayed = False

        # Initiate the App
        # Create a new window using the CTk class from the ...
        # ...customtkinter module
        self.window = customtkinter.CTk(fg_color="#2B2D31")
        # Set the title of the window
        self.window.title("ChatGPT Tkinter App")
        # Set the size of the window
        self.window.geometry("720x615")
        # Set the window icon
        self.window.iconbitmap("./icons/chat.ico")
        # Set dark mode
        customtkinter.set_appearance_mode("dark")
        # Set default color theme
        customtkinter.set_default_color_theme("blue")

        # Create a frame for the chat window and its attached scrollbar
        frame_chatwin = customtkinter.CTkFrame(
            master=self.window, fg_color="#2B2D31"
        )
        # Position the frame on the window
        frame_chatwin.pack(pady=40)

        # Create a chat window as a Text widget within the frame.
        # Set the background color (i.e. bg), width, border width ...
        # ...(i.e. bd), font color (i.e. fg), relief style, cursor color ...
        # ...(i.e. insertbackground), text wrapping (i.e. wrap), ...
        # ...and selection background color.
        self.chat_window = Text(
            master=frame_chatwin,
            bg="#313338",
            width=65,
            height=20,
            bd=1,
            fg="#BABCBE",
            relief="flat",
            insertbackground="#6699FF",
            wrap=WORD,
            selectbackground="#5865f2",
        )
        # Position the chat window inside the frame
        self.chat_window.grid(row=0, column=0)

        # Create a vertical scroll bar for the chat window
        scrollbar_chatwin = customtkinter.CTkScrollbar(
            master=frame_chatwin,
            orientation="vertical",
            command=self.chat_window.yview,
        )
        # Position the vertical scroll bar to the right side of chat window
        scrollbar_chatwin.grid(row=0, column=1, sticky=N + S + W)

        # Configure the chat window to use the scrollbar for vertical ...
        # ...scrolling, set the font to 'sans-serif', and disable the ...
        # ...manual entry into the chat window
        self.chat_window.configure(
            yscrollcommand=scrollbar_chatwin.set,
            font=("sans-serif"),
            state=DISABLED,
        )

        # Create an entry widget for the user to enter their message
        self.user_msg_entry = customtkinter.CTkEntry(
            master=self.window,
            fg_color="#313338",
            text_color="#BABCBE",
            placeholder_text="Type your message here and hit the 'Enter' key",
            width=585,
            height=50,
            border_width=1,
        )
        # Position the entry widget right below the chat window
        self.user_msg_entry.pack(pady=0)
        # Bind the activity of pressing the Enter key to the ...
        # ...send_text_message() function
        self.user_msg_entry.bind("<Return>", self.send_text_message)

        # Create a frame for 3 buttons
        frame_buttons = customtkinter.CTkFrame(
            master=self.window,
            fg_color="#2B2D31",
        )
        # Position the frame below the user message entry widget
        frame_buttons.pack(pady=35)

        # 'Update API Key' button
        # Create a button to update the API key. When clicked, it calls ...
        # ...the toggle_key_part() function
        update_key_button = customtkinter.CTkButton(
            master=frame_buttons,
            text="Update API Key",
            fg_color="#5865f2",
            hover_color="#2133ee",
            height=40,
            command=self.toggle_key_part,
        )
        # Position the button inside the frame
        update_key_button.grid(row=0, column=0, padx=0)

        # 'Listen To Message' button
        # Create a button to play the bot's message in audio. When ...
        # ...clicked, it calls the play_bot_message() function
        listen_button = customtkinter.CTkButton(
            master=frame_buttons,
            text="Listen To Message",
            fg_color="#5865f2",
            hover_color="#2133ee",
            height=40,
            command=self.play_bot_message,
        )
        # Position the button next to update key button
        listen_button.grid(row=0, column=1, padx=82)

        # 'Clear History' button
        # Create a button to clear the chat history while NOT ...
        # ...reinitializing the chatbot. When clicked, it calls ...
        # ...the clear_history() function
        clear_button = customtkinter.CTkButton(
            master=frame_buttons,
            text="Clear History",
            fg_color="#5865f2",
            hover_color="#2133ee",
            height=40,
            command=self.clear_history,
        )
        # Position the button next to listen button
        clear_button.grid(row=0, column=2, padx=0)

        # Create a frame for API key part
        # This frame will be shown or hidden by the update_key_button ...
        # ...and save_button
        self.frame_key = customtkinter.CTkFrame(
            master=self.window,
            border_width=1,
        )

        # Create an Entry widget for the user to enter their API key
        self.key_entry = customtkinter.CTkEntry(
            master=self.frame_key,
            placeholder_text="Enter you API key here",
            fg_color="#313338",
            text_color="#BABCBE",
            width=240,
            height=40,
            border_width=1,
        )
        # Position the key entry widget inside the frame_key
        self.key_entry.grid(row=0, column=0, padx=20, pady=20)

        # Set initial option for the model selection combobox
        self.model_var = customtkinter.StringVar(value="Select a GPT Model")
        # Create a ComboBox widget for the user to select a GPT model
        self.model_combobox = customtkinter.CTkComboBox(
            master=self.frame_key,
            values=[
                "Select a GPT Model",
                "gpt-3.5-turbo",
                "gpt-4o",
                "gpt-4-turbo",
            ],
            fg_color="#313338",
            button_hover_color="#5865f2",
            width=175,
            height=40,
            border_width=1,
            variable=self.model_var,
        )
        # Position the combobox inside the frame_key next to the key entry
        self.model_combobox.grid(row=0, column=1, padx=10)

        # Create 'Save Key' button for saving the entered API key. When ...
        # ...clicked, it calls the save_key() function
        save_key_button = customtkinter.CTkButton(
            master=self.frame_key,
            text="Save",
            width=68,
            height=40,
            fg_color="#5865f2",
            hover_color="#2133ee",
            command=self.save_key,
        )
        # Position the button inside the frame_key next to the combobox
        save_key_button.grid(row=0, column=2, padx=20)

        # Start the tkinter event loop, which keeps the application ...
        # ...running and handles user interactions
        self.window.mainloop()


    def send_text_message(self, event):
        """Event function that sends the user's message to the bot and
        display chat history inside the chat window.
        """
        # Get the text message from the user_msg_entry
        user_message = self.user_msg_entry.get()
        # Check if user's message is entered
        if user_message.strip():
            # If the API key is not provided
            if not self.KEY:
                # Display an error message that reminds the user to ...
                # ...enter their API key
                messagebox.showerror(
                    "API Key Not Provided",
                    "Please enter your API key to initiate your chat!",
                )
            # If the API key is provided
            else:
                # Enable text insertion into the chat window
                self.chat_window.config(state=NORMAL)
                # Insert the user's message into the chat window
                self.chat_window.insert(
                    END,
                    "You <{}>: ".format(
                        datetime.now().strftime("%H:%M:%S %Y/%m/%d")
                    )
                    + user_message
                    + "\n\n",
                )
                # Send the user's message to the bot for processing ...
                # ...and retrieve the bot's response
                self.bot_message = self.bot.respond(
                    user_message=user_message, model=self.MODEL
                )
                # Insert the bot's message into the chat window
                self.chat_window.insert(
                    END,
                    "Bot <{}>: ".format(
                        datetime.now().strftime("%H:%M:%S %Y/%m/%d")
                    )
                    + self.bot_message
                    + "\n\n",
                )
                # Disable text insertion into the chat window
                self.chat_window.config(state=DISABLED)
                # Clear the user message entry
                self.user_msg_entry.delete(0, END)


    def toggle_key_part(self):
        """Method to toggle the visibility of the API key part
        """
        # Toggle the state of key_part_displayed between True and False
        self.key_part_displayed = not self.key_part_displayed
        # Check if key_part_displayed is True and display the API key ...
        # ...part accordingly
        if self.key_part_displayed:
            # Display the API Key part
            self.show_key_part()
        else:
            # Hide the API Key part
            self.hide_key_part()


    def clear_history(self):
        """Method to clear the chat history and reset bot_message variable
        """
        # Enable text insertion into the chat window
        self.chat_window.config(state=NORMAL)
        # Reset bot_message to empty string
        self.bot_message = ""
        # Delete all messages in the chat window
        self.chat_window.delete(1.0, END)
        # Disable text insertion into the chat window
        self.chat_window.config(state=DISABLED)


    def play_bot_message(self):
        """Method to play the audio of the bot's message using the bot's
        text-to-speech functionality.
        """
        # If the API key is not provided...
        if not self.KEY:
            # Display an error message to enter a valid API key
            messagebox.showerror(
                "API Key Not Provided",
                "Please enter your API key to initiate your chat!",
            )
        else:
            # If the bot's message is not empty
            if self.bot_message.strip():
                # Play the audio of the bot's message
                self.bot.speak(self.bot_message)


    def show_key_part(self):
        """Method to display the API key part on the application window
        """
        # Expand the application window vertically to display the API key part
        self.window.geometry("720x740")
        # Display the frame for the API key part
        self.frame_key.pack(pady=8)
        # Set default value for API Key entry
        self.key_entry.insert(0, self.KEY)


    def hide_key_part(self):
        """Method to hide the API key part of the application window
        """
        # Clear the API Key entry
        self.key_entry.delete(0, END)
        # Restore the application window back to its original size
        self.window.geometry("720x615")
        # Remove the frame for API key part from the app window
        self.frame_key.pack_forget()


    def save_key(self):
        """Method to save the entered API key and initialize the chatbot with
        the new key.
        """
        # Check if the API key entry is not empty
        if self.key_entry.get().strip():
            # Check if the user has selected a valid GPT model
            if self.model_var.get() == "Select a GPT Model":
                # Display an error message to remind selecting a GPT model
                messagebox.showerror(
                    "GPT Model Not Selected",
                    "Please select a GPT model to initiate your chat!",
                )
            # If a valid GPT model is selected...
            else:
                # If API key input and selected GPT model both remain ...
                # ...the same
                if (self.key_entry.get() == self.KEY) and \
                   (self.model_var.get() == self.MODEL):
                    # Set key_part_displayed to False
                    self.key_part_displayed = False
                    # Hide the API key part
                    self.hide_key_part()
                # If the value in API key entry has been changed...
                else:
                    # Display a confirmation dialog to inform the user ...
                    # ...about the consequences of updating the API key
                    ToSaveKey = messagebox.askyesno(
                        "Update API Key and GPT Model",
                        (
                            "Updating the API key and/or GPT Model requires "
                            "RESTARTING the ChatBot, which will clear the chat "
                            "history. Are you sure you want to proceed?"
                        ),
                    )
                    # If the user confirms to update the API key
                    if ToSaveKey:
                        # Update the API Key
                        self.KEY = self.key_entry.get()
                        # Update the selected GPT model
                        self.MODEL = self.model_var.get()
                        # Clear the chat history
                        self.clear_history()
                        # Enable text insertion into the chat window
                        self.chat_window.config(state=NORMAL)
                        # Insert a message into the chat window indicating ...
                        # ...that the API key is being updated
                        self.chat_window.insert(
                            END, "[Updating API Key...]\n\n"
                        )

                        # Try start a new conversation with the chatbot
                        try:
                            # Instantiate the ChatBot with the new API key
                            self.bot = ChatGPTBot(self.KEY)
                            # Send a test message to the chatbot to ensure ...
                            # ...it is working
                            self.bot_message = self.bot.respond(
                                user_message="hello", model=self.MODEL
                            )
                            # If the chatbot is successfully loaded, display ...
                            # ...a success message in the chat window...
                            self.chat_window.insert(
                                END,
                                (
                                    "[Chatbot loaded successfully with the "
                                    f"{self.MODEL} model! You may begin "
                                    "your conversation now.]\n\n"
                                ),
                            )
                            # ...and the bot's response to the test message
                            self.chat_window.insert(
                                END,
                                "Bot <{}>: ".format(
                                    datetime.now().strftime(
                                        "%H:%M:%S %Y/%m/%d"
                                    )
                                )
                                + self.bot_message
                                + "\n\n",
                            )
                            # Set key_part_displayed flag to False
                            self.key_part_displayed = False
                            # Hide the API key part
                            self.hide_key_part()
                        # If the chatbot fails to initialize
                        except Exception as e:
                            # Reinitialize the 3 variables
                            self.bot = None
                            self.KEY = ""
                            self.bot_message = ""
                            # Clear the API Key entry
                            self.key_entry.delete(0, END)
                            # Insert an error message into the chat window ...
                            # ...indicating the specific error encountered
                            self.chat_window.insert(
                                END, "[ERROR: Invalid API key provided]\n\n"
                            )
                            # Set key_part_displayed to True
                            self.key_part_displayed = True
                            # Retain the API key part
                            self.show_key_part()
                            # Display an error message indicating the API ...
                            # ...key is invalid
                            messagebox.showerror(
                                "Invalid API Key",
                                (
                                    "API Key Invalid. Please ensure that a "
                                    "valid API key has been entered."
                                ),
                            )

                        # Disable text insertion into the chat window
                        self.chat_window.config(state=DISABLED)



# Run the ChatBot App
ChatBotApp = TkinterApp()
