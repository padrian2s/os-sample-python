from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Running model srv v1.0\n entry points /init /run /cleanup\n"

@application.route("/init")
def init():
    return "Initialize the model"
    
@application.route("/run")
def run():
    return "Running model...\nDone."
    
@application.route("/clean")
def clean():
    return "Cleanup...\nComplete!"

if __name__ == "__main__":
    application.run()
