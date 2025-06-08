import requests

API_KEY = "Your API key here"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat(instruction, text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": instruction},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        return f"🍳 ChefCat says:\n{content}"
    return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    print("🍳 ChefCat is ready! Type 'exit' to quit.")
    instruction = (
        "You are a friendly chef who explains Python like cooking recipes. "
        "You help Sakshi cook up simple and tasty Python code with easy steps!"
    )
    while True:
        user_text = input("You: ")
        if user_text.lower() == "exit":
            print("🍳 ChefCat says: Bon appétit, Sakshi! Come back for more tasty code soon!")
            break
        print("ChefCat:", chat(instruction, user_text))
