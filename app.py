from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html', result="")

@app.route('/', methods=['POST'])
def calculate():
    try:
        # Get the expression from the form
        expression = request.form['display']
        # Evaluate the expression
        result = eval(expression)
    except Exception as e:
        result = "Error"
    
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
