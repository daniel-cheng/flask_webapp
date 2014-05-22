from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
		print("HTML Accessed")
	return render_template('home.html')
 

@app.route('/stylesheet')
def stylesheet():
    with open("static\stylesheets\stylesheet.css", "r") as css:
        css_string = css.read()
	print("CSS Accessed")
    return css_string    

# if __name__ == '__main__':
	# print("Application started")
    # app.run()