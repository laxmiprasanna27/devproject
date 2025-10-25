from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('moon_weight.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight_input = request.form.get('weight')
    planet = request.form.get('planet')

    try:
        weight = float(weight_input)

        if planet == 'Moon':
            converted = weight * 0.165
            result = f"Your weight on the Moon would be: {converted:.2f} kg"
        else:
            converted = weight / 0.165
            result = f"Your weight on Earth would be: {converted:.2f} kg"

    except (ValueError, TypeError):
        result = "Please enter a valid number for weight!"

    return render_template('moon_weight.html', result=result)


if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)
