from flask import Flask, request, jsonify
import validator

app = Flask(__name__)

app.secret_key = "abcasdasdasdas"

@app.route('/validate', methods=['GET'])
def validate():
    no = request.headers.get('no')
    month = request.headers.get('month')
    year = request.headers.get('year')
    cvc = request.headers.get('cvc')

    if no is None:
        return jsonify({"error": "no not provided"}), 400
    
    if month is None:
        return jsonify({"error": "month not provided"}), 400

    if year is None:
        return jsonify({"error": "year is not provided"}), 400

    if cvc is None:
        return jsonify({"error": "cvc is not provided"}), 400

    card = validator.Card(no, int(month), int(year), int(cvc))

    if card.is_valid:
        return jsonify({"valid": "true", "brand": card.brand})
    else:
        return jsonify({"valid": "false"})


if __name__ == '__main__':
    app.run(debug=True)