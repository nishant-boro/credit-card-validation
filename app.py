from flask import Flask, request
import validator

app = Flask(__name__)

app.secret_key = "abcasdasdasdas"

@app.route('/validate', methods=['GET'])
def validate():
    
    return response()

if __name__ == '__main__':
    app.run(debug=True)