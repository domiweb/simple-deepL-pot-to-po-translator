import polib
import requests
import os
import time

# DeepL API Key (replace with your own API key)
DEEPL_API_KEY = "YOUR-DEEPL-API-KEY"
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"  # For free plan, or "https://api.deepl.com/v2/translate" for Pro


def translate_text(text, target_lang="DE", retries=3):
    """Translates a text using the DeepL API while preserving line breaks. Waits on 429 errors."""
    if not text.strip():  # If the text is empty, no translation is needed
        return text

    formatted_text = text.replace("\n", "<br>")  # Replace line breaks with HTML tag
    params = {
        "auth_key": DEEPL_API_KEY,
        "text": formatted_text,
        "target_lang": target_lang
    }

    for attempt in range(retries):
        response = requests.post(DEEPL_API_URL, data=params)
        time.sleep(0.3)  # Wait time of 200ms after each request

        if response.status_code == 200:
            translated_text = response.json()["translations"][0]["text"]
            return translated_text.replace("<br>", "\n")  # Restore line breaks
        elif response.status_code == 429:
            wait_time = (attempt + 1) * 5  # Exponential wait time
            print(f"429 Too Many Requests - Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Error during translation: {response.text}")
            return None  # Return None instead of the original text

    print("Maximum number of attempts reached. Translation not performed.")
    return None


def translate_pot_file(pot_file, output_po_file, target_lang="DE"):
    """Reads a .pot file, translates it, and saves the output as a .po file."""
    pot = polib.pofile(pot_file)

    for entry in pot:
        if entry.msgid and not entry.msgstr:  # Translate only untranslated entries
            print(f"Translating: {entry.msgid}")

            # If msgid is multiline, join it together
            original_text = "\n".join(entry.msgid.splitlines())
            translated_text = translate_text(original_text, target_lang)

            if translated_text is not None:
                # Convert translation back to multiline format
                entry.msgstr = "\n".join(translated_text.split("\n"))

    pot.save(output_po_file)
    print(f"Translated file saved: {output_po_file}")


if __name__ == "__main__":
    input_pot = input("Enter the path to the .pot file: ")
    output_po = input("Enter the path for the output .po file: ")
    target_language = input("Enter the target language (e.g., DE, FR, ES): ").upper()

    if not os.path.exists(input_pot):
        print(f"File {input_pot} not found!")
    else:
        translate_pot_file(input_pot, output_po, target_language)
