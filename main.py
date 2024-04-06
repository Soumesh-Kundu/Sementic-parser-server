from flask import Flask,request
from helper.spliter import spliter 
from time import time
app: Flask=Flask(__name__)

@app.route('/',methods=["GET"])
def hellworld():
    return {
        "hello": "world"
    }

@app.route('/api/sementics',methods=["POST"])
def getSementicSplit():
    if request.method!="POST":
        return 
    body=request.get_json()
    res=spliter(body.get('data'))
    return {
        "data":res
    }

@app.errorhandler(500)
def internal_error(error):
    print(error)
    return "internal server error",500
if __name__=="__main__":
    app.run(debug=True)