from flask import Flask
import logging
app = Flask(__name__)
 
@app.route('/')
def main_route():
 logging.info("in main route")
 return 'Hello World!'

@app.route('/home')
def second():
 logging.info("in home route")
 return "Bye."

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
