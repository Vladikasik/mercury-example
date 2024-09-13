from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    print(f"Received data: {data}")
    return "Data received", 200

if __name__ == '__main__':
    app.run(host='95.163.223.236', port=8080)