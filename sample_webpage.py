import os
from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def hello_world():
	print("HTML Accessed")
	return render_template('home.html')
 

# @app.route('/stylesheet')
# def stylesheet():
    # with open("static\stylesheets\stylesheet.css", "r") as css:
        # css_string = css.read()
	# print("CSS Accessed")
    # return css_string    
	
if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
 
