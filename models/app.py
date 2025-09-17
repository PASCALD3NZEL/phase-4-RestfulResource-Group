from flask import Flask
from config import db
from routes.course_routes import course_bp

app = Flask(__name__)
app.register_blueprint(course_bp)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
