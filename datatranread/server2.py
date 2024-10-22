from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Store the last received data
last_received_data = None

@app.route('/api/data', methods=['POST'])
def receive_data():
    logging.info("POST request received at /api/data")
    
    raw_data = request.data  # Get the raw request data
    logging.info("Raw data received: %s", raw_data.decode('utf-8'))  # Log raw data

    try:
        last_received_data = request.get_json(force=True)  # Parse the incoming JSON data
        logging.info("Received data: %s", last_received_data)  # Log the parsed JSON
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
    app.run(host='0.0.0.0', port=8000)