from flask import Flask, request, render_template
import requests

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="grammarly/coedit-large")

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/grammarly/coedit-large"
headers = {"Authorization": f"Bearer {'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'}"}


def query(dropdown_value, textinput_value):
    dict_map = {
        "option1": "Fix the grammar",
        "option2": "Make this text coherent",
        "option3": "Rewrite to make this easier to understand",
        "option4": "Paraphrase this",
        "option5": "Write this more formally",
        "option6": "Write in a more neutral way",
    }
    prompt = dict_map[dropdown_value] + ": " + textinput_value
    payload = {"inputs": prompt}
    response = pipe(prompt)

    return response[0]["generated_text"]


@app.route("/")
def home():
    return render_template("input.html")


@app.route("/submit", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        dropdown_value = request.form.get("dropdown")
        textinput_value = request.form.get("textinput")
        # Process the form data here
        processed_data = query(dropdown_value, textinput_value)
        print(processed_data)
        # Then redirect to the output page with the processed data
        return render_template("output.html", output=processed_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
# ruff: noqa
