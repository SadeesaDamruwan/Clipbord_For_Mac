Here's a README file for your Clipboard AI Search project, tailored for macOS users.

### README.md

```markdown
# Clipboard AI Search

This script monitors the clipboard for new content and sends it to the GPT-4 model for processing. The response is then copied back to the clipboard when `⌘+X` (Command+X) is pressed. The script can also be terminated using the hotkey `⌘+B` (Command+B).

## Prerequisites

- **Python 3.6+**
- **OpenAI API Key**
- **Required Python Packages**: `openai`, `pyperclip`, `python-dotenv`, `keyboard`

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/clipboard-ai-search.git
cd clipboard-ai-search
```

### 2. Create and Activate a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Required Packages

```sh
pip install -r requirements.txt
```

### 4. Set Up Your OpenAI API Key

- Create a `.env` file in the root directory of the project.
- Add your OpenAI API key to the `.env` file:

  ```env
  OPENAI_API_KEY=your_openai_api_key
  ```

## Usage

### 1. Run the Script

```sh
python main.py
```

### 2. Monitor the Clipboard

- The script will monitor the clipboard for new content.
- When new content is detected, it will be sent to the GPT-4 model for processing when `⌘+X` (Command+X) is pressed.
- The response will be copied back to the clipboard.

### 3. Terminate the Script

- Press `⌘+B` (Command+B) to terminate the script.

## Troubleshooting

- **Permission Issues**: Ensure you have the necessary permissions to read from and write to the clipboard. You may need to grant accessibility permissions to your terminal or Python environment in macOS settings.
- **Keyboard Library on macOS**: The `keyboard` library might require special permissions to monitor keyboard events. If you face any issues, try running the script with elevated privileges.


## Acknowledgments

- [OpenAI](https://openai.com) for the GPT-4 model.
- Libraries used: `openai`, `pyperclip`, `python-dotenv`, `keyboard`.
```

### Additional Notes:

- Replace `https://github.com/yourusername/clipboard-ai-search.git` with the actual URL of your repository.
- This README assumes that the script is named `main.py` and is located in the root directory of the project.

