# Translation Script for .POT Files using DeepL

This Python script automates the translation of `.pot` files using the DeepL API and saves the translated content as `.po` files. It ensures proper formatting by preserving line breaks and handles API request limits with retry logic.

## Features
- Translates text while maintaining line breaks.
- Uses the DeepL API for high-quality translations.
- Handles API request limits (429 errors) with exponential backoff.
- Processes `.pot` files and saves translated content as `.po` files.

## Prerequisites
Before using this script, ensure you have the following installed:
- Python 3.x
- Required dependencies:
  - `requests`
  - `polib`

You can install the required dependencies using pip:
```sh
pip install requests polib
```

## Getting Started

### 1. Clone the Repository
Initialize a Git repository and clone the script:
```sh
git init
# If you already have a repository, clone it
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Configure DeepL API Key
Edit the script and replace `YOUR-DEEPL-API-KEY` with your actual DeepL API key. If you are using a Pro plan, update the `DEEPL_API_URL` accordingly.

### 3. Run the Script
Execute the script to translate a `.pot` file:
```sh
python script.py
```
Follow the on-screen prompts to:
- Enter the path to the `.pot` file.
- Specify the output `.po` file path.
- Choose the target language (e.g., `DE` for German, `FR` for French).

### 4. Example Usage
Assume you have a `.pot` file located at `translations/messages.pot`. Run:
```sh
python script.py
```
Enter:
```
Path to the input .pot-file : translations/messages.pot
Path to the output .po-Datei ein: translations/messages.po
Translation language (e.g. DE, FR, ES): DE
```

The translated `.po` file will be saved at `translations/messages.po`.

## Error Handling
- If the DeepL API returns a 429 error (too many requests), the script will wait and retry.
- If the `.pot` file is not found, an error message is displayed.

## License
This project is licensed under the MIT License.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues!

---

### Author
Your Name (or Company Name)

