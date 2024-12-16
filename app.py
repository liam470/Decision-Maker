import openai
from flask import Flask, render_template, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Your OpenAI API Key (you must set your own key here)
openai.api_key = 'your_openai_api_key'

# Define a function to call the OpenAI API
def get_chatgpt_response(user_input):
    response = openai.Completion.create(
        model="text-davinci-003",  # You can change this to GPT-4 if needed
        prompt=user_input,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for interacting with the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = get_chatgpt_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
