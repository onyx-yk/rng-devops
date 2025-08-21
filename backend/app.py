from flask import Flask, jsonify, request
import random

app = Flask(__name__)
current_number = random.randint(1, 100)

@app.route('/api/random')
def random_number():
    global current_number
    if request.args.get('refresh') == 'true':
        current_number = random.randint(1, 100)
    
    return jsonify({"number": current_number})

@app.route('/')
def home():
    return "RNG API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)