from src.lc_openapi_poc.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


