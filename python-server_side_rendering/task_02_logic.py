from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json', 'r') as read_file:
        json_to_python_file = json.load(read_file)
    return render_template('items.html', items=json_to_python_file['items'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)