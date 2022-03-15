from flask import Flask, request, jsonify
import os, pickle, faker
from numpy import number

app = Flask(__name__)

# generate virtual person
details = faker.Faker()
name = details.name()

# load data
if not os.path.exists('data.pkl'):
    data = [
        {
            "number": "9096979834",
            "name": name,
            "done": False,
            "id": 1
        },
    ]
else:
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)

@app.route('/')
def main():
    return jsonify({'APIStatus': 'RUNNING'})

@app.route('/add-contact/', methods=['GET'])
def add_contact():
    print(request.args, data)
    try:
        new_contact = {
            "number": request.json['number'],
            "name": request.json['name'],
            "done": False,
            "id": len(data) + 1
        }
        data.append(new_contact)
        return jsonify({"status": "success", "data": new_contact})
    except IndexError:
        return jsonify({"status": "error", "message": "Invalid data"})

@app.route('/get-contacts/', methods=['GET'])
def get_contacts():
    print(request.args, data)
    return jsonify({"status": "success", "data": data})

@app.route('/set-done/', methods=['POST'])
def set_done():
    print(request.args, data)
    try:
        id = request.json['id']
        for contact in data:
            if contact['id'] == id:
                contact['done'] = True
                return jsonify({"status": "success", "data": contact})
        return jsonify({"status": "error", "message": "Invalid id"})
    except IndexError:
        return jsonify({"status": "error", "message": "Invalid data"})

if __name__ == '__main__':
    app.run(debug=True)

pickle.dump(data, open('_shared.pkl', 'wb'))
