import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
df = pd.read_csv("articles.csv")

user_data = {
    "Liked": [],
    "Disliked": [],
    "NotRead": [],
}

@app.route("/")
def index():
    return jsonify({
        "msg": "success"
    })

@app.route("/like")
def like():
    index = request.args.get("index")
    user_data["Liked"].append(index)
    user_data["Liked"].append(index)
    if index in user_data["Disliked"]:
        user_data["Disliked"].remove(index)
    return jsonify({
        "msg": "success"
    })

@app.route("/dislike")
def dislike():
    index = request.args.get("index")
    user_data["Disliked"].append(index)
    if index in user_data["Liked"]:
        user_data["Liked"].remove(index)
    return jsonify({
        "msg": "success"
    })

@app.route("/notread")
def notread():
    index = request.args.get("index")
    user_data["NotRead"].append(index)
    if index in user_data["Liked"]:
        user_data["Liked"].remove(index)
    if index in user_data["Disliked"]:
        user_data["Disliked"].remove(index)
    return jsonify({
        "msg": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
