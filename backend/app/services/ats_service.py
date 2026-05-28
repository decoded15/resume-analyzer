from app.prompts.ats_prompt import ATS_PROMPT
from app.services.gemini_service import generate_response
from app.utils.json_parser import parse_json_response


def analyze_ats_score(resume_data):

    final_prompt = ATS_PROMPT + str(resume_data)

    response = generate_response(final_prompt)

    parsed_response = parse_json_response(response)

    return parsed_response
