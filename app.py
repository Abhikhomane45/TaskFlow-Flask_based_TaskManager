from flask import Flask,request 

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "THIS IS ABOUT PAGE"

@app.route('/contact')
def contact():
    return "THIS IS Contact PAGE"

@app.route('/connect',methods=['GET','POST'])
def connect():
    if request.method == 'POST':
        return "POST request received"
    else:    
        return "GET request received"



if __name__ == '__main__':
    app.run(debug=True)