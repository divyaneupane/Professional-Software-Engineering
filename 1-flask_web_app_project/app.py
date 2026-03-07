from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/')
def home():
    return '<a href="/show-image">Load Image</a>'

@app.route('/bye')
def bye():
    return render_template('bye.html')

@app.route('/username/<name>')
def Learn(name):
    return f"Hello, {name}! Welcome to Flask Web App!"

@app.route('/<name>/<int:number>')
def learn(name, number):
    return f"Hello, {name}! You have entered the number {number}."

@app.route('/show-image')
def show_image():
    return render_template('image.html')

if __name__ == '__main__':
    app.run(debug=True)
