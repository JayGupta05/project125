from flask import Flask,jsonify,request
from Clf import get_prediction

app = Flask(__name__)
@app.route("/predict-alphabet",methods = ["POST"])
def pred () :
    img = request.files.get("alphabet")
    prediction = get_prediction(img)
    return jsonify({
        "prediction" : prediction
    }),200

if __name__ == "__main__":
    app.run(
        debug=True
    )