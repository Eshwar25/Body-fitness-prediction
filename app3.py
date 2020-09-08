from flask import Flask,render_template,request
import pickle
model=pickle.load(open('weight.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("base.html")
@app.route('/predict',methods=["POST"])
def func2():
    step_count=request.form['step_count']
    mood=request.form['mood']
    calories_burned=request.form['calories_burned']
    hours_of_sleep=request.form['hours_of_sleep']
    bool_of_active=request.form['bool_of_active']
    data=[[int(step_count),int(mood),int(calories_burned),int(hours_of_sleep),int(bool_of_active)]]
    pred=model.predict(data)
    print(pred)
    return render_template("base.html",y=str(pred))
if __name__=='__main__':
    app.run(debug= True)#wsgi local server url