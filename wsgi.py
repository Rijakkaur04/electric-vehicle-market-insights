"""
WSGI Entry Point for Production Cloud Deployments
Works seamlessly on Render, Railway, Vercel, PythonAnywhere, Heroku, AWS, and Docker.
"""

import os
from web_app.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

