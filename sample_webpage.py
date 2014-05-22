from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html')
	
def hello_world1():
    with open("templates\home.html", "r") as html:
        html_string = html.read()
    return html_string      

@app.route('/stylesheet')
def stylesheet():
    with open("static\stylesheets\stylesheet.css", "r") as css:
        css_string = css.read()
    return css_string    

if __name__ == '__main__':
    app.run(debug=True)