import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    # A porta 5000 casa com o API_URL definido em frontend/js/api.js
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=app.config.get("DEBUG", False),
    )
