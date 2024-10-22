from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Store the last received data
last_received_data = None

@app.route('/api/data', methods=['POST'])
def receive_data():
    global last_received_data
    try:
        last_received_data = request.get_json(force=True)  # Parse the incoming JSON data
        if not last_received_data or 'calories' not in last_received_data:
            return jsonify({"error": "Missing 'calories' in request data."}), 400
        
        logging.info("Received data: %s", last_received_data)  # Log received data
        return jsonify({"status": "success", "received": last_received_data}), 200

    except Exception as e:
        logging.error("Error processing request: %s", str(e))
        return jsonify({"error": "Invalid JSON format."}), 400

@app.route('/api/data', methods=['GET'])
def get_data():
    if last_received_data is not None:
        return jsonify(last_received_data), 200
    else:
        return jsonify({"error": "No data received yet."}), 404

if __name__ == '__main__':
    # Use environment variable for debug mode
    app.run(host='0.0.0.0', port=int(os.getenv("FLASK_PORT", 8000)), debug=os.getenv("FLASK_DEBUG", "0") == "1")