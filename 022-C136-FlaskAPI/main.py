import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
df = pd.read_csv("main.csv")
df_list = df.to_dict(orient="records")

@app.route("/")
def index():
    return jsonify({
        "data": df_list,
        "msg": "success"
    })

@app.route("/find")
def find():
    name = request.args.get("name")
    if name is None:
        return jsonify({
            "msg": "error"
        })
    else:
        for i in df_list:
            if i["name"] == name:
                return jsonify({
                    "data": i,
                    "msg": "success"
                })
        return jsonify({
            "msg": "error"
        })

if __name__ == '__main__':
    app.run(debug=True)
