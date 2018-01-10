# NWEA Assignment

I thought I'd do something completely out of the ordinary, and also make this assigment as easy as it could be. 

I used Python with the Flask Framework. I also had to use SQLite, and yeah like I've seen this more and more use JSON. The frontend should only use JSON, which is of coorse quite simple with AngularJS or React, since these data formats are easy to understand and read. The LICENSE file in the assignment was for the use of apache 2.0, but we don't use apache here, it's all covered my the simple python script.

What you actually only need is here is  the file 'nwea_server.py', the database 'posts.db' and the command 'curl' on Linux  to test the API. I also included the '''example''' file 'new_entry.json' to be used for the POST data to add a new entry. Of course the font end application will simply have to to a POST of that same data format, but we are writing the API here only.

# Set up the environment
On your linux system, run the following commands
* virtualenv nwea
* source nwea/bin/activate
* pip install flask flask-jsonpify flask-sqlalchemy flask-restful
* pip freeze

# Once you have the environment, on a new shell, you can do: 
* source nwea/bin/activate
* bin/python nwea_server.py

# Run the test
* to show ALL the posts in the database: 
 curl http://localhost:5010/showPosts 
* to show one single post by it's id (if it exists), the example will show post_id = 2:
 curl http://localhost:5010/showPosts/2
* to add a new post, use the file 'new_entry.json':
 curl-H "Content-type: application/json" -X  POST http://localhost:5010/addPost --data @new_entry.json 
