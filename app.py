from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)