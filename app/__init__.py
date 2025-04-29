from flask import Flask
from datetime import datetime
from app.routes import bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    @app.context_processor
    def inject_year():
        return {'year': datetime.now().year}
    
    return app
