from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        if os.path.exists('items.json') and os.path.getsize('items.json') > 0:
            with open('items.json', 'r') as read_file:
                json_to_python_file = json.load(read_file)
            
            items_list = json_to_python_file.get('items', [])

        else:
            items_list = []
        
        return render_template('items.html', items=items_list)

    except Exception as error:
        print(f"Error: {error}")
        return render_template('items.html', items=[])

if __name__ == '__main__':
    app.run(debug=True, port=5000)