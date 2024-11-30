from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        try:
            with open('products.json', 'r') as json_file:
                python_file = json.load(json_file)
        
        except FileNotFoundError:
            return render_template('product_display.html', error_message="JSON file not found")

    elif source == 'csv':
        try:
            with open('products.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                python_file = [row for row in reader]
                print(python_file)

        except FileNotFoundError:
            return render_template('product_display.html', error_message="CSV file not found")

    else:
        return render_template('product_display.html', error_message="Wrong source")

    if id:
        python_file = [product for product in python_file if str(product['id']) ==  str(id)]
        if not python_file:
            return render_template('product_display.html', error_message="Failed: Product not found in CSV source")

    return render_template('product_display.html', products=python_file)


if __name__ == '__main__':
    app.run(debug=True, port=5000)