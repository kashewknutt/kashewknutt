import google.generativeai as genai
import json
from datetime import date
from pathlib import Path
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

PROMPT = """
Generate a Turing Test question.

Rules:
- Output TWO short paragraphs (1–2 lines each)
- One must sound like a real human developer
- One must sound like AI-generated corporate fluff
- Do NOT say which is which in the text
- Language should be subtle and realistic

Return STRICT JSON ONLY:
{
  "option_a": "...",
  "option_b": "...",
  "answer": "A" or "B"
}
"""

response = model.generate_content(PROMPT)
text = response.text.strip()

# Gemini sometimes wraps JSON in ``` — strip it safely
text = text.replace("```json", "").replace("```", "")

data = json.loads(text)

A = data["option_a"]
B = data["option_b"]
answer = data["answer"]

today = date.today().isoformat()

svg = f"""
<svg width="600" height="360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="20" fill="#0d1117"/>

  <text x="300" y="40" text-anchor="middle"
        font-size="22" fill="#A302F7" font-weight="bold">
    Daily Turing Test
  </text>

  <a href="./{'correct' if answer == 'A' else 'wrong'}.svg">
    <rect x="40" y="70" width="520" height="90" rx="12" fill="#161b22"/>
    <text x="60" y="110" font-size="14" fill="#c9d1d9">{A}</text>
  </a>

  <a href="./{'correct' if answer == 'B' else 'wrong'}.svg">
    <rect x="40" y="190" width="520" height="90" rx="12" fill="#161b22"/>
    <text x="60" y="230" font-size="14" fill="#c9d1d9">{B}</text>
  </a>

  <text x="300" y="340" text-anchor="middle"
        font-size="12" fill="#8b949e">
    {today}
  </text>
</svg>
"""

Path("game/history").mkdir(exist_ok=True)

if Path("game/question.svg").exists():
    Path("game/question.svg").rename(f"game/history/{today}.svg")

Path("game/question.svg").write_text(svg)
