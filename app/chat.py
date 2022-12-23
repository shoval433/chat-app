from flask import Flask,render_template, request 
from datetime import datetime 

app = Flask(__name__)
#general chat
@app.route('/')
def get_no_room():
    return render_template("index.html")

@app.route('/<room>')
def get_room(room):
    return render_template("index.html")

@app.route("/chat/<room>")
def have_room(room):
    try:
        f=open("logs_"+room,'x')
    except:
        pass
    return render_template('index.html')


#The GET and POST of the chat 
@app.route("/api/chat/<room>",methods=['POST', 'GET'])
def chat(room):
    if request.method == 'GET':
        f = open("logs_"+room)
        return f

    elif request.method == 'POST':
        f = open("logs_"+room,"a+")
        timeData=datetime.now().strftime("%H:%M:%S")
        usr_massge = "["+timeData +"] "+request.form['username']+':'+request.form['msg']+'\n'
        f.write(usr_massge)
        return "200"

if __name__=="__main__":
    app.run(host="0.0.0.0")