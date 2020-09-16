#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def abc():
    return render_template('ram.html')
@app.route('/detail',methods=['GET','POST'])
def bob():
    if(request.method=='POST'):
        a=int(request.form['num1'])
        b=int(request.form['num2'])
        result=a+b
        return render_template('ram.html',mobile=result)
if __name__=="__main__":
    app.run()
    





# In[ ]:




