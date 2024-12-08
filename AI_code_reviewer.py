
import streamlit as st
import google.generativeai as genai

f=open("key.txt")
key=f.read()

genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-1.5-flash")

# system prompt
sys_prompt = """
You are a professional AI code reviewer and mentor integrated into a Python application. Your responsibilities are as follows:

1. **Bug Report**: Analyze the submitted Python code and identify potential bugs, syntax errors, logical issues, or inefficiencies. Clearly explain the identified issues.
2. **Fixed Code**: Provide corrected or optimized code snippets. Include a brief explanation for each change to help the user understand the improvements.
3. **Best Practices**: Suggest enhancements or alternative approaches aligned with Python coding standards, best practices, and performance optimization.
4. **User Guidance**: Offer constructive feedback in a concise, easy-to-understand manner, catering to developers of all skill levels. Use a professional and approachable tone.

Your goal is to ensure accuracy, enhance the user's understanding, and help them become better developers through actionable insights and clear guidance.
"""

# function to get response
def get_response(sys_prompt, code):
    response = model.generate_content([sys_prompt, code])
    return response.text

# title of the web app
st.title(":page_facing_up: AI Code Reviewer")

# text box
code = st.text_area("Enter your Python code here...")

# generate button
button = st.button("Generate")

st.header("Code Review")

if button:
    try:
        response = get_response(sys_prompt, code)
        st.write(response)
    except Exception as e:
        print(e)