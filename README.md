# ChatGPT-3.5 Desktop App

[![GitHub][github_badge]][github_link]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)](https://chat.openai.com/)


Welcome to the repository for the unofficial ChatGPT-3.5 Desktop App! This user-friendly application allows you to have natural language conversations 
with ChatGPT directly from your local computer. This desktop application is built upon OpenAI's **gpt-3.5-turbo model**, which offers advanced natural 
language processing capabilities. Through an intuitive user interface, you can easily engage in conversations with ChatGPT, review past interactions, 
and even listen to the chatbot's responses through audio playback. The goal of this app is to provide an immersive and enjoyable conversational experience that 
closely resembles interacting with a real person.

## Features

- **Intuitive User Interface**: The ChatGPT-3.5 Desktop App provides a seamless and user-friendly interface, enabling effortless conversations with ChatGPT.
- **Immersive Conversational Experience**: Engage in natural language conversations with ChatGPT using your own [OpenAI API key](https://platform.openai.com/account/api-keys), creating an authentic and immersive experience that closely resembles conversing with a real person.
- **Conversation History**: Easily access and review your past conversations within the app, allowing for convenient reference and continuity.
- **Audio Playback**: Enhance your experience by listening to the chatbot's responses through built-in audio playback functionality, bringing the conversation to life.

## Repository Structure

The repository is structured as follows:

- **MAIN.py**: This file is the main entry point of the desktop app and contains the Python code responsible for handling the user interface and communication with the ChatGPT model.
- **bot.py**: This file contains the Python code that defines the class for the ChatGPTBot, encapsulating the functionality of the ChatGPT model and handling the generation of responses.
- **0 - MUST READ FIRST.txt**: This file contains instructions for installing and running the application. It is recommended to read this file before proceeding with the installation.
- **requirements.txt**: This file lists all the required Python modules and packages necessary to run the desktop app. You can install these dependencies by running the command `pip install -r requirements.txt` as mentioned in the installation instructions later.
- **icons**: This folder contains the ICO image that is used as the app's window icon.
- **README.md**: Provides an overview of this repository.
- **LICENSE**: The license file for the project.


## Get Started

To intall the desktop application on your computer, please follow these steps:

1) Clone this repository to your local machine using the following command:
    ```
    git clone https://github.com/MaxineXiong/ChatGPT-3.5-Desktop-App.git
    ```
    Alternatively, you can download the EXE application from the web application **[Talk to GPT-3.5](https://maxinexiong-openai-api-web-apps-home-xbxlm8.streamlit.app/Talk_To_GPT3.5)**.

2) Download and install the latest version of [Python](https://www.python.org/downloads/) for your system. Make sure to select the "Add Python to PATH" option during the installation process.

3) Navigate to the project folder using File Explorer, type `cmd` in the address bar at the top of the window, and press Enter. This will open Command Prompt in the project folder.

4) Install all required Python modules and packages by running the following command in Command Prompt:
    ```
    pip install -r requirements.txt
    ```
5) Launch the desktop app by typing the following command in Command Prompt:
    ```
    python MAIN.py
    ```


Now you can start chatting with ChatGPT by entering your [API key](https://platform.openai.com/account/api-keys), and then typing your messages in the input field and pressing Enter.

## Contributions

Contributions to the ChatGPT-3.5 Desktop App are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request. Your contributions can help improve the functionality and user experience of the app.

## License

The ChatGPT-3.5 Desktop App is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute the application in accordance with the terms of the license.

## Acknowledgments

I would like to express my gratitude to the open-source community for their invaluable contributions. The development of this app would not have been possible without the support and efforts of the following projects and individuals:

- [OpenAI](https://openai.com/) for developing the ChatGPT 3.5 model.
- [Python](https://www.python.org/) for providing a powerful programming language.
- [GitHub](https://github.com/) for hosting this repository and enabling collaboration.

Thank you for using the ChatGPT 3.5 Desktop App! I hope you find it useful and enjoy your conversations with ChatGPT.


[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/MaxineXiong
