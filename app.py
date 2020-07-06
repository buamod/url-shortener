from flask import Flask, render_template, request

app = Flask(__name__)

## pass info from route to jinia tempalate as a second argument
## like shown below name='STRING'

@app.route('/')
def home():
    return render_template('home.html', name='home page')


## code=request.args['code']) when working with a port use .form instead of args 
## like code=request.form['code'])

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not Vaild'


@app.route('/about')
def about():
    return 'This is a url shortener'