# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("Index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
           # reading the inputs given by the user
           age = float(request.form['age'])

           hours_per_week = float(request.form['hours_per_week'])

           education = (request.form['education'])
           count = {'Some-college': 0, 'Preschool': 1, '5th-6th': 2, 'HS-grad': 3, 'Masters': 4, '12th': 5, '7th-8th': 6, 'Prof-school': 7, '1st-4th': 8, 'Assoc-acdm': 9, 'Doctorate': 10, '11th': 11,'Bachelors': 12, '10th': 13, 'Assoc-voc': 14,'9th': 15}
           key_list = list(count.keys())
           val_list = list(count.values())
           val = key_list.index(education)
           Education = val_list[val]

           marital_status = (request.form['marital_status'])
           count = {'Married-spouse-absent': 0, 'Widowed': 1, 'Married-civ-spouse': 2, 'Separated': 3, 'Divorced': 4, 'Never-married': 5, 'Married-AF-spouse': 6}
           key_list = list(count.keys())
           val_list = list(count.values())
           val = key_list.index(marital_status)
           marital = val_list[val]

           occupation = (request.form['occupation'])
           count = {'Farming-fishing': 1, 'Tech-support': 2, 'Adm-clerical': 3, 'Handlers-cleaners': 4, 'Prof-specialty': 5, 'Machine-op-inspct': 6, 'Exec-managerial': 7, 'Priv-house-serv': 8, 'Craft-repair': 9, 'Sales': 10, 'Transport-moving': 11, 'Armed-Forces': 12, 'Other-service': 13, 'Protective-serv':14}
           key_list = list(count.keys())
           val_list = list(count.values())
           val = key_list.index(occupation)
           Occupation = val_list[val]

           sex = (request.form['sex'])
           count = {'Male': 0, 'Female': 1}
           key_list = list(count.keys())
           val_list = list(count.values())
           val = key_list.index(sex)
           Sex = val_list[val]

           filename = 'xgboost_model.pickle'
           model = pickle.load(open(filename, 'rb'))
           scalerfile = 'scaler_model.pickle'
           scaler = pickle.load(open(scalerfile, 'rb'))
           scaled_data = scaler.transform([[age,hours_per_week,Education,marital,Occupation,Sex]])
           prediction = model.predict(scaled_data)
           print('prediction value is ', prediction)
           # showing the prediction results in a UI
           return render_template('predict.html', prediction = prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

