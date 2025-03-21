from flask import Flask
from flask_restful import Api
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models import Base

#   CREATE THE FLASK APP
app = Flask(__name__)

#   CREATE THE API OBJECT
api = Api(app)



engine = create_engine('sqlite:///database.db?check_same_thread=False', echo=False)
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
Base.metadata.create_all(engine)

#   DEFINE RESOURCES


if __name__ == '__main__':
    app.run(debug=True)