"""
Tests if API token works and if any output is returned

"""
import requests



API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": f"Bearer {'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'}"}


def test_api():
    """checks hugging api token works"""
    test_payload = {"inputs": "Testing"}
    response = requests.post(API_URL, headers=headers, json=test_payload)
    assert 'generated_text' in response.json()[0]


if __name__ == "__main__":
    test_api()