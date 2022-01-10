from flask import Flask,jsonify,request

app = Flask(__name__)
datas=[
        {
            "Contact": "9987644456",
            "Name": "Kush",
            "done" : False,
            "id" : 1
        },
        {
            "Contact": "9876543222",
            "Name": "Rahul",
            "done" : False,
            "id" : 2
        }
    ]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': datas[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    datas.append(task)
    return jsonify({
        "status":"success",
        "message": "data added succesfully!"
    })
    
        
def get_task():
    return jsonify({ "data" : datas })

if (__name__ == "__main__"): 
    app.run()