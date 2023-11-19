from flask import Flask, jsonify
from flask_cors import CORS
from controller.headlinesController import HeadlinesController

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

headlinesController = HeadlinesController()

@app.route('/')
def index():
    return jsonify(message="Hello from Flask!")

@app.route('/api')
def api():
    headlines = headlinesController.getHeadlines()
    return jsonify(headlines.serialize())

@app.route('/headline/<id>')
def headline(id):
    headline = headlinesController.getHeadlineById(id)
    return jsonify(headline.serialize())

if __name__ == '__main__':
    app.run(debug=True)
