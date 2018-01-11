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
* nwea/bin/python nwea_server.py

# Run the test (local)
* to show ALL the posts in the database: 
 _$ curl http://localhost:5010/showPosts_ 
* to show one single post by it's id (if it exists), the example will show post_id = 2:
 _$ curl http://localhost:5010/showPosts/2_
* to add a new post, use the file 'new_entry.json':
 _$ curl -H "Content-type: application/json" -X  POST http://localhost:5010/addPost --data @new_entry.json_

# requirements for post data
Make sure that your data is already url encoded, like the title: "Paul's blog" should be "Paul%27s blog". Just make sure that at least the single quotes are encoded!. There is a javascript encodeURI() function that you could use in your frontend, and should do the job!


# Run the LIVE test on AWS from your own linux box (or if you have curl on wiindows, that will work too) 
* to show ALL the posts in the database: 
 _$ curl http://ec2-52-27-248-102.us-west-2.compute.amazonaws.com:5010/showPosts_ 
* to show one single post by it's id (if it exists), the example will show post_id = 2:
 $ curl http://ec2-52-27-248-102.us-west-2.compute.amazonaws.com:5010/showPosts/2_
* to add a new post, use the file 'new_entry.json' (MAKE SURE YOU HAVE THAT FILE LOCALLY!!!!):
 _$ curl -H "Content-type: application/json" -X  POST http://ec2-52-27-248-102.us-west-2.compute.amazonaws.com:5010/addPost --data @new_entry.json_
 If you do NOT have the file, you can simply put something on the command line, like:
 _$ curl -H "Content-type: application/json" -X  POST http://ec2-52-27-248-102.us-west-2.compute.amazonaws.com:5010/addPost --data '[{"title":"title1","body":"new body"}]'_
 
**NOTE**: the LIVE test will not work after 02/01/2018 !!!!!!!!!

**NOTE**: Check also the same challange written in NodeJS at: https://github.com/pauldenijs/nwea_nodejs
