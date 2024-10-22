from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the last received data
last_received_data = None

@app.route('/api/data', methods=['POST'])
def receive_data():
    global last_received_data
    last_received_data = request.get_json()  # Parse the incoming JSON data
    print("Received data:", last_received_data)  # Print the received data to the console
    return jsonify({"status": "success", "received": last_received_data}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    if last_received_data is not None:
        return jsonify(last_received_data), 200
    else:
        return jsonify({"error": "No data received yet."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)