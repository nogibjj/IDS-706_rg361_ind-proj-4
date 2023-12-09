import requests

API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": f"Bearer {'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'}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query(
    {
        "inputs": "Fix the grammar: When I grow up I start to understand what he said is quite right.",
    }
)
print(output[0]["generated_text"])
