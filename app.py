from flask import Flask, request, jsonify, render_template
import openai
import json

app = Flask(__name__, template_folder="templates", static_folder="static", instance_relative_config=True)

api_key = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/initial_message')
def initial_message():
    with open("app/initial_message.json", "r") as f:
        initial_message_data = json.load(f)
    return jsonify(initial_message_data)

message_history = []

@app.route("/chat", methods=["POST"])
def chat():
    global api_key, message_history
    user_input = request.form.get("input")

    if api_key is None:
        api_key = request.form.get("api_key")
        openai.api_key = api_key

    # Append the new user input to message_history
    message_history.append({"role": "user", "content": user_input})
    
    # Your Chat-GPT logic here
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    response = completion.choices[0].message.content  # Replace with the actual response from Chat-GPT
    message_history.append({"role": "assistant", "content": response})
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
