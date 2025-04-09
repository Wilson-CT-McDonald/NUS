from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask"

@app.route('/home/<userid:number>')
def main_page(userid):
    return render_template('index.html',name=userid)

@app.route('/about')
def about():
    return "<html><body><h1>About Page</h1></body></html>"

if __name__ == '__main__':
    app.run(debug=True)