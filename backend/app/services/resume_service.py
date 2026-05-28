from app.prompts.structure_prompt import STRUCTURE_PROMPT
from app.services.gemini_service import generate_response
from app.utils.json_parser import parse_json_response

def extract_resume_data(cleaned_text):

    final_prompt = STRUCTURE_PROMPT + cleaned_text

    response = generate_response(final_prompt)

    parsed_response = parse_json_response(response)

    return parsed_response