import pickle

from flask import Flask, request, jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    print(json_)
    data = pd.DataFrame(json_, index=[0])
    # Load your pre-trained model
    model = pickle.load(open("model2.pkl","rb"))
    # Make predictions
    predictions = model.predict(data)
    predList = jsonify({'predictions': predictions.tolist()})
    normal_alert = 'Normal'
    Aggressive_alert = 'Please Drive slow!'
    if predictions[0] == 1:
        return jsonify({'Alert': normal_alert})
    elif predictions[0] == 2:
        return jsonify({'Alert': Aggressive_alert})
    #
    # return jsonify({'predictions': predictions.tolist()})

@app.route('/hello', methods=['GET'])
def hello():
    return "<p> RAGHAV </p>"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
