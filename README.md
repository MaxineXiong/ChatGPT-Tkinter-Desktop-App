# ChatGPT Tkinter Desktop App

[![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/MaxineXiong)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://www.python.org)
[![OpenAI API](https://img.shields.io/badge/OpenAI_API-E5E4E2?logo=OpenAI&logoColor=%23000000)](https://openai.com/blog/openai-api)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-00A67E?logo=openai)](https://chat.openai.com/)

<br/>

Welcome to the repository for the **unofficial ChatGPT Tkinter Desktop App**! This user-friendly application allows you to have natural language conversations
with [ChatGPT](https://openai.com/index/chatgpt) directly from your local computer — provided you have internet access. Built upon OpenAI's [**Chat Completions API**](https://platform.openai.com/docs/guides/text-generation/chat-completions-api), it leverages advanced natural language processing capabilities to deliver high-quality responses to human's requests.
Through an intuitive user interface, you can easily select between [***GPT-3.5 Turbo***](https://platform.openai.com/docs/models/gpt-3-5-turbo) and [***GPT-4 Turbo***](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4) models, engage in conversations with ChatGPT, review previous interactions,
and even listen to the chatbot's responses through audio playback. The goal of this application is to provide an immersive and enjoyable conversational experience that
closely resembles interacting with a real person.

***Press the CTRL key and click the badge below simultaneously to run the application** (Please be aware that the audio playback functionality may not be available when running the application on Replit)*:

[![Run on Repl.it](https://replit.com/badge/github/MaxineXiong/ChatGPT-Tkinter-Desktop-App.git)](https://replit.com/@MaxineXiong/ChatGPT-Tkinter-Desktop-App?v=1)

<br/>

## Features

- **Intuitive User Interface**: The **ChatGPT Tkinter Desktop App** provides a seamless and user-friendly interface, enabling effortless conversations with ChatGPT.
- **Immersive Conversational Experience**: Engage in natural language conversations with ChatGPT using your own [OpenAI API key](https://platform.openai.com/api-keys), creating an authentic and immersive experience that closely resembles conversing with a real person.
- **Model Selection**: Choose between the **GPT-3.5 Turbo** and **GPT-4 Turbo** models to tailor the conversational capabilities to your specific needs, ensuring optimal performance and accuracy.
- **Conversation History**: Easily access and review your past conversations within the app, allowing for convenient reference and continuity.
- **Audio Playback**: Enhance your experience by listening to the chatbot's responses through built-in audio playback functionality, bringing the conversation to life.

<br/>

## Repository Structure

The repository is structured as follows:
```
ChatGPT-Tkinter-Desktop-App/
├── MAIN.py                   
├── bot.py                   
├── requirements.txt         
├── icons/
├── virtual/         
├── README.md                 
└── LICENSE                   
```

- **MAIN.py**: This file is the main entry point of the desktop app and contains the Python code responsible for handling the user interface and communication with the GPT model.
- **bot.py**: This file contains the Python code that defines the class for the ChatGPTBot, encapsulating the functionality of the ChatGPT model and handling the generation of responses.
- **requirements.txt**: This file lists all the required Python modules and packages necessary to run the desktop app. You can install these dependencies by running the command `pip install -r requirements.txt` as mentioned in the installation instructions later.
- **icons/**: This folder contains the ICO image that is used as the app's window icon.
- **virtual/**: This folder contains all files related to the virtual environment, facilitating an isolated space for Python package management.
- **README.md**: Provides an overview of this repository.
- **LICENSE**: The license file for the project.

<br/>

## Get Started

To intall the desktop application on your computer, please follow these steps:

1) Clone this repository to your local machine using the following command:
    ```
    git clone https://github.com/MaxineXiong/ChatGPT-Tkinter-Desktop-App.git
    ```
    Alternatively, you can download the EXE application from the web application **[Talk to GPT](https://maxinexiong-openai-api-web-apps-home-xbxlm8.streamlit.app/Talk_To_GPT)**.

2) Download and install the latest version of [Python](https://www.python.org/downloads/) for your system. Make sure to select the "Add Python to PATH" option during the installation process.

3) Navigate to the project folder using File Explorer, type `cmd` in the address bar at the top of the window, and press Enter. This will open Command Prompt in the project folder.

4) Now launch the desktop application within the virtual environment by entering the following command in the Command Prompt:
    ```
    virtual\Scripts\python MAIN.py
    ```


Now you can start chatting with ChatGPT by entering your API key and selecting a GPT model, and then typing your messages in the input field and pressing Enter.

https://github.com/MaxineXiong/ChatGPT-Tkinter-Desktop-App/assets/55864839/089cf277-d42f-4d85-800f-7b75dbc39684

<br/>

## Contributions

Contributions to the **ChatGPT Tkinter Desktop App** are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request. Your contributions can help improve the functionality and user experience of the app.

<br/>

## License

The **ChatGPT Tkinter Desktop App** is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute the application in accordance with the terms of the license.

<br/>

## Acknowledgments

I would like to express my gratitude to the open-source community for their invaluable contributions. The development of this app would not have been possible without the support and efforts of the following projects and individuals:

- [OpenAI](https://openai.com/) for developing GPT models and APIs.
- [Python](https://www.python.org/) for providing a powerful programming language.
- [GitHub](https://github.com/) for hosting this repository and enabling collaboration.

<br/>

Thank you for using the **ChatGPT Tkinter Desktop App**! I hope you find it useful and enjoy your conversations with ChatGPT.


