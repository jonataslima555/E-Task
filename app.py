from flask import Flask
from routes.account import account_bp
from routes.tasks import task_bp
app = Flask(__name__)

app.register_blueprint(account_bp)
app.register_blueprint(task_bp)


if __name__ == "__main__":
    app.run(debug=True)
    