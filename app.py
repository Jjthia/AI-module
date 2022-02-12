#!/usr/bin/env python
# coding: utf-8

# # FLASK 

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS")
        pred = model.predict([[float(rates)]])
        print(pred)
        s = "The predicted DBS share price is " + str(pred[0][0])
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result="2"))


# To run jupyter file. 
# - must ensure the http://127.0.0.1:5000/ put into the frontend in html
# - 5000 is port, if the port cannot then 80 or 111

# In[ ]:


if __name__ == "__main__":
    app.run()

