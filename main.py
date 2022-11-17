from flask import Flask, jsonify

app = Flask(__name__)

books_db =[
    {
        'name':'secret',
        'price': 400
    },
    {
        'name':'Deep work ',
        'price':500
    }
]

#retrive all books
@app.route('/')
def home(): 
    return jsonify ({'Message':'Welcome'})


@app.route('/on')
def on():
    return jsonify ({'state':'1'})

@app.route('/off')
def off():
    return jsonify ({'state':'0'})

#retrive one books
#create a books

app.run(port=5500)