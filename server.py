from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('no_ninja.html')

@app.route('/ninja')
def show_all_ninja():
    return render_template('ninja.html', color="")

@app.route('/ninja/<color>')
def show_ninja_color(color):
    return render_template('ninja.html', color=color)

app.run(debug=True)
