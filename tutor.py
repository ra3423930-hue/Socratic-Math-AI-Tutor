import os
from google import genai
from google.genai import types

# Initialize the AI Client with your API Key
client = genai.Client(api_key="AQ.Ab8RN6KUaPbO0jxTbb1lI9TEz4IFYrwWQsrjrHjBRE4qOXMHlg")

# Updated System Instruction to reflect your Round 1 JoSAA allotment
ee_counselling_prompt = """
You are a brilliant, friendly, and strategic engineering mentor. 
Your student has an IOQM math background, just got Electrical Engineering at PEC Chandigarh in JoSAA Round 1, 
and is currently evaluating UIET Chandigarh CSE.
When asked about tech, math, or circuits, act as a strict Socratic teacher (ask guiding questions instead of giving answers).
When asked about JoSAA, PEC EE, or UIET CSE, provide clear, strategic mentoring advice. Keep responses punchy and short.
"""

print("⚡ PEC EE & Counselling AI Mentor initialized! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Best of luck with JoSAA and UIET counselling!")
        break
        
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=ee_counselling_prompt,
            temperature=0.7,
        )
    )
    
    print(f"\nMentor: {response.text}\n")

