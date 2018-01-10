from flask import Flask, url_for, request, json
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify


db_connect = create_engine('sqlite:///blog.db')
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/showPosts')
def showPosts():
    conn = db_connect.connect() # connect to database
    query_string="SELECT * FROM posts"
    query = conn.execute(query_string)
    result = {'allData': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return jsonify(result)

    
@app.route('/showPosts/<postid>')
def ShowPost(postid):
    conn = db_connect.connect() # connect to database
    query_string="SELECT * FROM posts WHERE post_id='" + postid + "'"
    query = conn.execute(query_string)
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return jsonify(result)

@app.route('/addPost', methods = ['POST'])
def addPost():
    #return "JSON Message: " + json.dumps(request.json)
    data=json.loads(json.dumps(request.json))
    #print type(data)
    title=''
    body=''
    for i in data:
	title=i['title']
	body=i['body']
    conn = db_connect.connect() # connect to database
    query_string="INSERT INTO posts (title,body) VALUES('" + title + "','" + body + "')"
    query = conn.execute(query_string)
    return "Data inserted"
	

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5010)

