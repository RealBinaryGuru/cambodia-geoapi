from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/provinces")
def get_provinces():
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "provinces.json"

    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {"message": "Provinces data file not found."}, 404
    except json.JSONDecodeError as e:
        return {"message": f"Error decoding JSON: {str(e)}"}, 500
    except Exception as e:
        return {"message": f"An unexpected error occurred: {str(e)}"}, 500
