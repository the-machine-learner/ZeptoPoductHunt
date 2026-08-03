"""
Groq LLM API Client & Dynamic Riddle Generation Pipeline.
"""

import streamlit as st
import requests
import json
import time
import os

def get_groq_api_key():
    """Retrieve Groq API key from Streamlit Secrets or Environment Variable."""
    if "GROQ_API_KEY" in st.secrets:
        return st.secrets["GROQ_API_KEY"]
    return os.getenv("GROQ_API_KEY", "")

@st.cache_data(show_spinner=False, ttl=600)
def generate_ai_clue(persona, target_prod, clue_stage, current_history):
    """
    Generate a dynamic riddle clue using Groq LLM (llama-3.1-8b-instant).
    Enforces Progressive Simplification rules based on clue_stage (1, 2, or 3).
    Cached for 10 minutes to prevent Groq API rate limiting.
    """
    start_t = time.time()
    api_key = get_groq_api_key()
    
    # Progressive difficulty rules:
    if clue_stage == 1:
        diff_rule = "Clue 1 (Clever Riddle): Write a clever, witty, non-obvious riddle. Do NOT explicitly name the product title or brand. Make the user think!"
    elif clue_stage == 2:
        diff_rule = "Clue 2 (Simpler Hint): Make this clue SIMPLER and MORE HELPFUL. Give a clear hint about its product category, shape, or daily usage benefit."
    else:
        diff_rule = "Clue 3 (Direct Actionable Clue): Make this clue VERY DIRECT and EASY TO SOLVE. Explicitly point the user to the exact aisle/category and how it helps them finish the hunt!"

    prompt = f"""
You are the AI Game Engine for Zepto Product Hunt Week.
Generate a personalized, witty riddle clue for the customer.

USER PROFILE:
- Name: {persona['name']} ({persona['title']})
- Demographics: {persona['demographics']}
- Tone Preference: {persona['tone']}
- Current Purchase History: {', '.join(current_history)}
- Suggested Adjacent Categories: {', '.join(persona.get('suggested_categories', []))}

TARGET PRODUCT FOR THIS HUNT STAGE:
- Name: {target_prod['name']}
- Category: {target_prod['category']}
- Description: {target_prod['desc']}

CLUE PROGRESSION STAGE:
- Clue Number: {clue_stage} of 3
- Rule: {diff_rule}

STRICT JSON OUTPUT FORMAT (Return ONLY valid JSON):
{{
  "clue_title": "Short 3-5 word catchphrase in ALL CAPS (e.g. THE GHOST IN THE LIVING ROOM)",
  "riddle": "1-2 sentence witty riddle matching the user tone",
  "hint": "Short 2-4 word category hint (e.g. Hint: Check Gaming)"
}}
"""

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "response_format": {"type": "json_object"}
            },
            timeout=8
        )
        latency = round((time.time() - start_t) * 1000, 1)
        if response.status_code == 200:
            res_data = response.json()
            content = res_data["choices"][0]["message"]["content"]
            parsed = json.loads(content)
            parsed["latency_ms"] = latency
            parsed["model"] = "llama-3.1-8b-instant"
            parsed["prompt_used"] = prompt
            return parsed
        else:
            raise Exception(f"Groq API Error {response.status_code}: {response.text}")
    except Exception as e:
        # Graceful fallback if offline or no key
        return {
            "clue_title": f"CLUE {clue_stage}: MYSTERY CHALLENGE",
            "riddle": f"Looking for an upgrade in {target_prod['category']}? Discover {target_prod['name']} in your catalog!",
            "hint": f"Hint: Check {target_prod['category']}",
            "latency_ms": 0,
            "model": "fallback",
            "error": str(e)
        }
