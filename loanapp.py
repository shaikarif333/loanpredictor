import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

 
with open('models.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_loan(income, credit_score):
   
    additional_features = [0, 0, 0, 0, 0, 0, 0, 0] 
    input_data = [[income, credit_score] + additional_features] 

    prediction = model.predict(input_data)[0]
    return prediction

    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        income = float(request.form['income'])
        credit_score = float(request.form['credit_score'])
        prediction = predict_loan(income, credit_score)

  
        loan_status = "Loan Approved" if prediction == 1 else "Loan Declined"

        return render_template('result.html', prediction=loan_status)
    return render_template('loan.html')


if __name__ == '__main__':
    app.run(debug=True)