from flask import Flask, request, jsonify
import pandas as pd

df = pd.read_csv('articles.csv')
df = df.sort_values(by='n_actions', ascending=False).head(10)

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "ok",
    })

@app.route('/articles')
def articles():
    return jsonify({
        "status": "ok",
        "articles": df.to_dict('records')
    })

if __name__ == '__main__':
    app.run(debug=True)
