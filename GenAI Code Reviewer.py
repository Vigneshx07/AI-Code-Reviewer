import streamlit as st
import openai

openai.api_key = "AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI"

def review_code(code):
    prompt = f"""
    Review the following Python code and identify any potential bugs, errors, or improvements.
    Provide a brief explanation of the issue and suggest a corrected version of the code.
    
    Code:
    {code}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI code reviewer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

def main():
    st.title("GenAI Code Reviewer")
    st.write("Submit your Python code for AI-powered review.")
    
    code_input = st.text_area("Enter your Python code:", height=300)
    
    if st.button("Review Code"):
        if code_input.strip():
            with st.spinner("Reviewing code..."):
                feedback = review_code(code_input)
                st.subheader("AI Feedback:")
                st.write(feedback)
        else:
            st.warning("Please enter some code to review.")
    
if __name__ == "__main__":
    main()
