import openai
import sys
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from the .env file

# Replace with your own API key
openai.api_key = os.getenv("OPENAI_API_KEY") #"your-api-key"

# get command line from GPT-3 from prompt
# davinci: completion model: single round
# gpt-3.5-turbo: chat model
def get_command(prompt):
    #response = openai.Completion.create( # single turn: text completion models only
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # engine
#        prompt=f"Translate the following English description to a Linux command: {prompt}",
        messages=[
            {"role": "system", "content": """
            You are a helpful assistant that translates an English request into Linux commands. 
            Please respond at most 3 lines of code, strictly in the following format:
            # comment explaining the suggested commands 
            # comment explaining their options, if any. This line is optional.
            actual suggested commands
            """},
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature=0.5,
        max_tokens=100,
        #top_p=1,
        #frequency_penalty=0,
        #presence_penalty=0,
    )

   # command = response.choices[0].text.strip()
    command = response['choices'][0]['message']['content'].strip()
    return command

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nl2cmd.py <natural_language_description>")
        sys.exit(1)

    #prompt = sys.argv[1]
    prompt = ' '.join(sys.argv[1:])
    command = get_command(prompt)
    #print(f"Suggested command: {command}")
    print(f"{command}")
