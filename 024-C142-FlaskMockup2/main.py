from flask import Flask, request, jsonify

import contentbased_filtering as cbf
import demographic_filtering as df

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "success",
        "data": cbf.df.to_dict('records')
    })

@app.route('/popular')
def popular():
    return jsonify({
        "status": "success",
        "data": df._articles
    })

@app.route('/search')
def search():
    title = request.args.get('title')
    return jsonify({
        "status": "success",
        "data": cbf.get_recommendations(title)
    })

if __name__ == '__main__':
    app.run(debug=True)
