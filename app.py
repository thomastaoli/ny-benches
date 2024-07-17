import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory, jsonify

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv('PROJECT_API_KEY')

# Print the API key to the console for debugging
print(f"Loaded API_KEY: {API_KEY}")

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/key', methods=['GET'])
def get_api_key():
    return jsonify({'apiKey': API_KEY})

if __name__ == '__main__':
    app.run(debug=True)
