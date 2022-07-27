
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add") 
def add_two_numbers():
    """return the sum of the two numbers passed in"""
    
    # nums = request.args["a","b"] 
    a = request.args["a"]
    b = request.args["b"]
        
    return f"{add(int(a),int(b))}"

@app.get("/sub") 
def subtract_two_numbers():
    """return the difference of the two numbers passed in"""
    
    # nums = request.args["a","b"] 
    a = request.args["a"]
    b = request.args["b"]
        
    return f"{sub(int(a),int(b))}"

@app.get("/mult") 
def multiply_two_numbers():
    """return the product of the two numbers passed in"""
    
    # nums = request.args["a","b"] 
    a = request.args["a"]
    b = request.args["b"]
        
    return f"{mult(int(a),int(b))}"

@app.get("/div") 
def divide_two_numbers():
    """return the quotient of the two numbers passed in"""
    
    # nums = request.args["a","b"] 
    a = request.args["a"]
    b = request.args["b"]
        
    return f"{div(int(a),int(b))}"
