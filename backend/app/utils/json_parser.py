import json
import re

def parse_json_response(response_text):

    cleaned_response = re.sub(r"```json|```", "", response_text).strip()

    return json.loads(cleaned_response)