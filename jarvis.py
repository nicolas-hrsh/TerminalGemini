import os
import google.generativeai as genai
import re


#
def formatted_txt(text):
    # Headings: Convert "# Heading" to "Heading" (bold)
    text = re.sub(r'# (.+)', r'\033[1m\1\033[0m\n', text)
    
    # Bold: Convert "**bold**" to bold text
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\033[1m\1\033[0m', text)
    
    # Italics: Convert "*italic*" to italic text
    text = re.sub(r'\*([^\*]+)\*', r'\033[3m\1\033[0m', text)
    
    # Lists: Convert "- item" to "• item"
    text = re.sub(r'^- (.+)', r'• \1', text, flags=re.MULTILINE)
    
    # Inline Code: Convert `code` to styled code (optional)
    text = re.sub(r'`([^`]+)`', r'\033[40m\033[1m\1\033[0m', text)

    return text
# # #
genai.configure(api_key="AIzaSyCF1_hxd-iuNql_iyftjcjZ0WVBdgu7Sn8")

input1 = input("Question: ")
input2 = input("Response type: ")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

small_text = "Answer should be small and precise."
normal_text = " Answer should be in bullet points"
elaborated_text = "Answer should be step by step well formatted. Use bullet points as well."

if input2 == 's':
  input1 += small_text
elif input2 == 'n':
  input1 += normal_text
elif input2 == 'e':
  input1 += elaborated_text
else:
  input1 = input1 + "Answer normally."


response = chat_session.send_message(input1)
response = formatted_txt(response.text)
print(response)