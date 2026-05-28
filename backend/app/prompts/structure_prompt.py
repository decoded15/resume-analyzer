STRUCTURE_PROMPT = """
Extract the following information from the resume.
Return ONLY valid JSON.
Required structure:
{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "experience": [],
  "education": [],
  "projects": [],
  "certifications": []
}

Resume Text:
"""