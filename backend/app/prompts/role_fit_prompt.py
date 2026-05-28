ROLE_FIT_PROMPT = """
You are an expert AI resume evaluator.

Evaluate how well this resume matches the target job role.

Analyze:
1. Skill alignment
2. Experience relevance
3. Domain fit
4. Technical readiness
5. Resume strengths for this role
6. Missing skills for this role

Return ONLY valid JSON.

Format:

{
  "role_fit_score": 0,
  "matching_skills": [],
  "missing_skills": [],
  "role_fit_summary": "",
  "improvement_recommendations": []
}

Target Role:
"""
