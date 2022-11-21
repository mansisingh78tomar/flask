from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/')
def home(): 
    return jsonify ({'Message':'Welcome'})


@app.route('/on')
def on():
    return jsonify ({'state':'1'})

@app.route('/off')
def off():
    return jsonify ({'state':'0'})

if __name__=='__main__':
    app.run(debug=True)
