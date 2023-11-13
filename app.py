from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        lift_type = request.form['lift_type']
        weight_lifted = float(request.form['weight_lifted'])
        repetitions = int(request.form['repetitions'])

        # Calculate 1RM using the Epley formula
        one_rep_max = weight_lifted * (1 + (repetitions / 30))

        return render_template('result.html', lift_type=lift_type, one_rep_max=one_rep_max)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
