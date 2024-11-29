import os
import openai

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def review_and_refactor_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Review and refactor the following code:\n\n{code}"}
        ],
        max_tokens=1500,
        temperature=0.5,
    )

    suggestions = response.choices[0].message['content'].strip()
    print(f"Suggestions for {file_path}:\n{suggestions}")

if __name__ == "__main__":
    # Example: Review and refactor all Python files in the src directory
    for root, _, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                review_and_refactor_code(os.path.join(root, file))