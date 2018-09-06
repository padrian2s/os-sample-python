from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    try:
     fr = open('/data/dataset.txt', 'r').read()
    except:
     fr = "no storage attached"
    return "Running model srv v1.0.1\n entry points \n /init \n /run \n /cleanup \n\n\n file content: \n %s" % (fr)

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
