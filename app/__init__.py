from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app) # Enable CORS for all routes
    app.config.from_object(config_class)

    # Register Blueprints
    from app.routes.candidate_routes import candidate_bp
    from app.routes.analysis_routes import analysis_bp
    from app.routes.job_routes import job_bp
    
    app.register_blueprint(candidate_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(job_bp)

    @app.route('/')
    def index():
        return {"message": "AI Candidate Evaluation Engine API is running"}

    return app
