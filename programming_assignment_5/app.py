from flask import Flask, request, jsonify
from datetime import datetime
import random 
import csv

app = Flask(__name__)

@app.route("/fact", methods=["GET"])
def fact():

    fun_facts = []
    with open("random_fun_facts.csv", "r") as file: 
        facts = csv.reader(file)
        for row in facts:
            fun_facts.append(str(row)) 
    amount = request.headers.get("amount", "1")
    return_facts = ""
    for i in range(int(amount)):
        curr_choice = random.randrange(0, len(fun_facts) - 1)
        return_facts = return_facts + str(fun_facts.pop(curr_choice)) + "\n"
        #fun_facts.remove(fun_facts[curr_choice])
    return str(return_facts) 

@app.route("/info", methods=["GET"])
def info():
    current_time = datetime.now().isoformat()
    user_agent = request.headers.get("User-Agent")
    method = request.method

    return_vals = f"Time: {current_time} \n User Agent: {user_agent} \n Method: {method}\n"

    return return_vals 

if __name__ == "__main__":
    app.run()
