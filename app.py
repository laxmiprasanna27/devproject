from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')  # keep this HTML file in templates folder

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
