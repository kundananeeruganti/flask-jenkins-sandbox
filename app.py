from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/mock-data', methods=['GET'])
def get_mock_data():
    mock_response = {
        "status": "success",
        "data": {
            "project": "DevOps Sandbox",
            "tech_stack": ["Python", "Flask", "Docker", "Jenkins"],
            "message": "Hello from inside VS Code!"
        }
    }
    return jsonify(mock_response), 200

@app.route('/api/v1/mock-data2', methods=['GET'])
def get_mock_data2():
    mock_response = {
        "status": "success",
        "data": {
            "message": "Hello from inside VS Code!"
        }
    }
    return jsonify(mock_response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)