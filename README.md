# Folder Structure Logger

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Folder Structure Logger** is a Python-based application that helps you analyze and visualize the folder structure of any directory. It provides a graphical interface for users to select a folder, view its contents in a tree-like format, and automatically copies the structure to the clipboard. The app also saves the folder structure in a log file for future reference.

## Features:
- Analyze and visualize folder structures.
- Automatically copy the folder structure to clipboard.
- Save folder structure in a log file.
- User-friendly interface built using Tkinter.
- Option to view a tutorial on first launch.
  
## Badges
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Installation

To use the Folder Structure Logger, follow these steps:

1. **Clone this repository:**

   ```bash
   git https://github.com/ridwan-arch-v/Map_Folder_path.git
   cd Map_Folder_path
   ```

2. **Install dependencies:**

   Make sure you have Python 3.7+ installed. You can install the required dependencies with `pip`:

   ```bash
   pip install pyperclip
   ```

3. **Run the application:**

   After the dependencies are installed, you can run the application by executing:

   ```bash
   python app.py
   ```

## How to Use

1. **Launch the Application:**

   When you first run the application, you will be greeted with a tutorial window. You can choose to continue with the tutorial or skip it.

2. **Choose a Folder:**

   After the tutorial (or on subsequent runs), click on the "Pilih Folder" (Select Folder) button. A file dialog will open where you can navigate to and select the folder whose structure you want to analyze.

3. **View Folder Structure:**

   The folder structure will be displayed in a tree-like format in the main window. It will show all the directories and files inside the selected folder.

4. **Copy to Clipboard:**

   The folder structure will be automatically copied to the clipboard once the process is complete. You can then paste it anywhere you like.

5. **Save to Log File:**

   The folder structure is saved in a log file in the same directory as `app.py`. The file is named `struktur_<folder_name>.txt`, where `<folder_name>` is the name of the selected folder.

6. **Repeat Process:**

   You can select a different folder and repeat the process to analyze other directories.

## Test

> ![ilustration](/test/test.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tkinter: For creating the graphical interface.
- Pyperclip: For copying content to the clipboard.

---
