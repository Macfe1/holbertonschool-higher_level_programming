from flask import Flask, render_template, request
import json, csv, sqlite3

# databsae setting
def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL  
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
    conn.close()

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

    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, category, price FROM Products')
            rows = cursor.fetchall()
            python_file = [
                {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
                for row in rows
            ]
        except sqlite3.Error as error:
            return render_template('product_display.html', error_message=f"Database error: {error}")
        finally:
            conn.close()
    else:
        return render_template('product_display.html', error_message="Wrong source")

    if id:
        python_file = [product for product in python_file if str(product['id']) ==  str(id)]
        if not python_file:
            return render_template('product_display.html', error_message="Failed: Product not found in source")

    return render_template('product_display.html', products=python_file)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)