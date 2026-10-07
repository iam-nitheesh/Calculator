from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = ""
    
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        try:
            # eval() safely calculates the basic math expression string
            # We restrict it to numbers and basic operators for safety
            allowed_chars = set("0123456789+-*/.()")
            if all(c in allowed_chars for c in expression):
                result = eval(expression)
            else:
                result = "Error: Invalid Characters"
        except Exception as e:
            result = "Error"
            
    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)