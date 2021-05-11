from flask import Flask, request, make_response, jsonify


app = Flask(__name__)


@app.route('/login')
def log():
    auth = request.authorization()
    print(auth)

if __name__ == '__main__':
    app.run(debug=True)