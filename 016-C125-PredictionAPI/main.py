from flask import Flask, request, jsonify
import pickle
from predict import get_prediction

app = Flask(__name__)
model = pickle.load(open('_saved/model0.pkl', 'rb'))

@app.route('/')
def main():
    return jsonify({'APIStatus': 'RUNNING'})

@app.route('/predict/', methods = ['POST'])
def predict():
    try:
        data = request.files.get("digit")
        prediction = get_prediction(data, model)
        return jsonify({'prediction': prediction[0]})
    except IndexError:
        return jsonify({'prediction': 'Invalid data'})

if __name__ == '__main__':
    app.run(debug=True)

