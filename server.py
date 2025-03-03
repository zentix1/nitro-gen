from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_nitro_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

@app.route('/generate', methods=['GET'])
def generate():
    codes = [f"https://discord.gift/{generate_nitro_code()}" for _ in range(5)]
    return jsonify({"codes": codes})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
