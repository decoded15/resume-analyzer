from app.prompts.structure_prompt import STRUCTURE_PROMPT
from app.services.gemini_service import generate_response


def extract_resume_data(cleaned_text):

    final_prompt = STRUCTURE_PROMPT + cleaned_text

    response = generate_response(final_prompt)

    return response