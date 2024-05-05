from flask import Flask,request, render_template
import numpy as np
import pickle
import sklearn
print(sklearn.__version__)
#loading models
dtr = pickle.load(open('decisiontree.pkl','rb'))
preprocessor = pickle.load(open('preprocessor1.pkl','rb'))

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Crop = request.form['Crop']
        Crop_Year = request.form['Crop_Year']
        Season = request.form['Season']
        State = request.form['State']
        Area = request.form['Area']
        Annual_Rainfall = request.form['Annual_Rainfall']
        Fertilizer  = request.form['Fertilizer']
        

        features = np.array([[Crop,Crop_Year,Season,State,Area,Annual_Rainfall,Fertilizer]],dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features).reshape(1,-1)

        return render_template('index.html',prediction = prediction)

if __name__=="__main__":
    app.run(debug=True)


