from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'Contact':998764456,
        'name':"Raju",
        'done':False,
        "id":1
    },
    {
        'Contact':9876543222,
        'name':"Rahul",
        'done':False,
        "id":2
    }
]
@app.route('/add-data',methods=['Post'])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':"succes",
        'message':'task added succesfully'
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        "data":tasks
    })
if(__name__=="__main__"):
    app.run(debug=True)