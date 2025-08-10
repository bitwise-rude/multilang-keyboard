-----

# Multilanguage-Typer

A simple Python application that acts as a real-time translator for text input and clipboard content. This tool was originally created to make communication easier on platforms like Omegle, allowing for seamless conversation with people from different countries without constantly switching between a separate browser-based translator.

-----

## Usage ⌨️

1.  **Start the application:** Run `main.py`. A small window with an ON/OFF button will appear.
2.  You can also use the pre-compiled 'UkraineEasy.exe' inside the dist folder. It is precompiled for Ukrainian
3.  **Turn it on:** Click the button to activate the translator. The button's text will turn green.
4.  **To translate what you type:**
      - Type your message in any text field (e.g., a chat box).
      - Press the **`Insert`** key.
      - The application will automatically delete your original text and paste the translated version.
5.  **To translate copied text:**
      - Simply copy text to your clipboard.
      - The translated text will appear in a pop-up alert box.

<img width="426" height="235" alt="image" src="https://github.com/user-attachments/assets/84af27e9-da6e-4eae-b0b8-c9ded2007d6d" />

-----

## Technologies Used 💻

  - **Python:** The core language for the application.
  - **`tkinter`:** Used to create the simple graphical user interface (GUI) with an ON/OFF button.
  - **`googletrans`:** A library that provides an API for translating text using Google Translate.
  - **`pynput`:** Used to listen for keyboard events (keystrokes).
  - **`pyautogui`:** A library for programmatically controlling the mouse and keyboard, used here for typing and displaying alerts.
  - **`pyperclip`:** Provides a cross-platform way to copy and paste text.
  - **`threading`:** Allows for the clipboard monitoring to run in the background without freezing the GUI.

-----

## How it Works 🧠

The application operates in two main modes: a typing translator that listens for keystrokes and a clipboard translator that monitors copied text. The `Insert` key acts as a trigger to translate what you have typed. A separate background thread handles the clipboard monitoring to avoid freezing the app's GUI.

-----

## Setup and Installation ⚙️

### Prerequisites

  - Python 3.6+
  - `pip` (Python package installer)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/multilanguage-typer.git
    cd multilanguage-typer
    ```
2.  **Install the required libraries:**
    ```bash
    pip install googletrans==4.0.0-rc1 pynput pyautogui pyperclip
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```

-----

## Executable Files 📦

A pre-compiled executable, **`UkraineEasy.exe`**, is included in the `dist` folder. This version of the application is specifically configured to translate to and from the Ukrainian language, making it ready to use without any setup.
