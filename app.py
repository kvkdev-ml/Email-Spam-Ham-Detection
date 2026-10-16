from flask import Flask, render_template,request,jsonify
from flask_cors import CORS
import pickle as pk
app=Flask(__name__)
CORS(app)
@app.route('/')
@app.route('/DiabCare')
def index():
    return render_template('diabetes.html')
@app.route('/api/diabetes',methods=['POST'])
def diabetes_prediction():
    data = request.get_json()
    email = data["email"]
    with open('transform_model.pkl','rb') as mf:
        vectorizer=pk.load(mf)
    with open("email_model.pkl", "rb") as f:
        model = pk.load(f)
    ip = vectorizer.transform([email])
    prediction = 1 if model.predict(ip)[0]=='spam' else 0
    return jsonify({
        "predicion":prediction,
        "confidence":97
    })
if __name__=='__main__':
    app.run()