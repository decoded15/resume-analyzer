import re

def clean_resume_text(text):

    # Remove excessive empty lines
    text = re.sub(r"\n\s*\n", "\n\n", text)

    # Replace multiple spaces with single space
    text = re.sub(r"[ \t]+", " ", text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text