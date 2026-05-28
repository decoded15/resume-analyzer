from app.prompts.role_fit_prompt import ROLE_FIT_PROMPT
from app.services.gemini_service import generate_response
from app.utils.json_parser import parse_json_response
from app.models.role_fit_model import RoleFitAnalysis


def analyze_role_fit(resume_data, target_role):

    final_prompt = (
        ROLE_FIT_PROMPT
        + target_role
        + "\n\nResume Data:\n"
        + str(resume_data)
    )

    response = generate_response(final_prompt)

    parsed_response = parse_json_response(response)

    validated_response = RoleFitAnalysis(**parsed_response)

    return validated_response.model_dump()