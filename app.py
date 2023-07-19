from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('transactions.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL)''')

# Commit the changes and close the connection
conn.commit()
conn.close()


@app.route('/history')
def transaction_history():
    # Retrieve all transactions from the database
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()
    
    # Pass the transactions to the template
    return render_template('history.html', transactions=transactions)


@app.route('/', methods=['GET','POST'])
def calculate_cost():
    if request.method == 'POST':
        amount = float(request.form['amount'].replace(',',''))
        
        # Save the amount in the database
        conn = sqlite3.connect('transactions.db')
        c = conn.cursor()
        c.execute("INSERT INTO transactions (amount) VALUES (?)", (amount,))
        conn.commit()
        conn.close()
        
        # Perform calculations for transaction costs
        
        cost_app = amount*3/100

        cost_ussd = amount*5/100

        cost_otc = amount*6/100


        
        # Return the results to the template
        return render_template('result.html', amount = '{0:,.2f}'.format(amount), cost1= '{0:,.2f}'.format(cost_app), cost2 = '{0:,.2f}'.format(cost_ussd), cost3 = '{0:,.2f}'.format(cost_otc),
                saving_1 = '{0:,.2f}'.format(cost_ussd - cost_app), saving_2 = '{0:,.2f}'.format(cost_otc - cost_app)

            )
    
    return render_template('index.html')
