from flask import Flask, jsonify, redirect, url_for
from app.routers.profile_router import profile_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(profile_bp)
    
    @app.route('/')
    def index():
        # Option 1: Return a welcome message
        return jsonify({
            "message": "Welcome to Git Profile API",
            "endpoints": {
                "profile": "/profile?github_org=<org_name>&bitbucket_team=<team_name>"
            },
            "example": "/profile?github_org=mailchimp&bitbucket_team=mailchimp"
        })
        
        # Option 2: Redirect to the profile endpoint with example parameters
        # return redirect(url_for('profile.get_profile', github_org='mailchimp', bitbucket_team='mailchimp'))
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404
        
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
