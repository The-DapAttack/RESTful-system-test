from flask import Flask
from flask_restful import Api

#   CREATE THE FLASK APP
app = Flask(__name__)

# CREATE THE API OBJECT
api = Api(app)



if __name__ == '__main__':
    app.run(debug=True)