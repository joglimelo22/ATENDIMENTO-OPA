from flask import Flask, url_for

# Blueprint imports
from routes.home import home_blueprint
from routes.sendMessage import sendMessage_blueprint



app = Flask(__name__)


app.register_blueprint(home_blueprint)
app.register_blueprint(sendMessage_blueprint)


if "__main__" == __name__:
    app.run(debug=True)