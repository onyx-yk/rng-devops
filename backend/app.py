from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random')
def random_number():
    return jsonify({"number": random.randint(1, 100)})

@app.route('/')
def home():
    return "RNG API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
