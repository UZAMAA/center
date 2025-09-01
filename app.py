# Main Flask application file
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Define the path for the data file
DATA_FILE = os.path.join('data', 'database.json')

# Ensure the data directory and file exist
os.makedirs('data', exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    """Read and return data from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({})

@app.route('/api/data', methods=['POST'])
def save_data():
    """Receive data and save it to the JSON file."""
    new_data = request.get_json()
    if new_data is None:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400

    with open(DATA_FILE, 'w') as f:
        json.dump(new_data, f, indent=4)

    return jsonify({"status": "success", "message": "Data saved successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
