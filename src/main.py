from fastapi import FastAPI, Query
from pathlib import Path
import csv

from response import BaseResponse

app = FastAPI(
    title="Cam GeoAPI",
    description="This is a sample API with FastAPI and Swagger",
    version="1.0.0"
)


@app.get("/provinces", tags=['Provinces'])
def get_provinces(name: str = Query(None, description="Name of the province to search for")):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Province.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            provinces = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                }
                for row in csv_reader
            ]

        if name:
            provinces = [
                province for province in provinces
                if name.lower() in province["name_en"].lower() or name.lower() in province["name_km"].lower()
            ]

            if not provinces:
                return BaseResponse.error(message="No matching provinces found", status_code=404)

            return BaseResponse.success(message="Matching provinces retrieved successfully", data=provinces)

        return BaseResponse.success(message="Data retrieved successfully", data=provinces)

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/provinces/{code}", tags=['Provinces'])
def get_province_by_code(code: str):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Province.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                if row[1] == code:
                    province = {
                        "type": row[0],
                        "code": row[1],
                        "name_km": row[2],
                        "name_en": row[3],
                    }
                    return BaseResponse.success(message="Province retrieved successfully", data=province)

        return BaseResponse.error(message="Province with the specified code not found", status_code=404)

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/districts", tags=['Districts'])
def get_districts(name: str = Query(None, description="Name of the district to search for")):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "District.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            districts = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "province_id": row[4],
                }
                for row in csv_reader
            ]

        if name:
            districts = [
                district for district in districts
                if name.lower() in district["name_en"].lower() or name.lower() in district["name_km"].lower()
            ]

            if not districts:
                return BaseResponse.error(message="No matching districts found", status_code=404)

            return BaseResponse.success(message="Matching districts retrieved successfully", data=districts)

        return BaseResponse.success(message="Data retrieved successfully", data=districts)

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/districts/{code}", tags=['Districts'])
def get_district_by_code(code: str):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "District.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                if row[1] == code:
                    district = {
                        "type": row[0],
                        "code": row[1],
                        "name_km": row[2],
                        "name_en": row[3],
                        "province_id": row[4],
                    }
                    return BaseResponse.success(message="District retrieved successfully", data=district)

        return BaseResponse.error(message="District with the specified code not found", status_code=404)

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/districts/province/{province_id}", tags=['Districts'])
def get_districts_by_province_id(province_id: str):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "District.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            districts = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "province_id": row[4],
                }
                for row in csv_reader
                if row[4] == province_id
            ]

        if not districts:
            return BaseResponse.error(
                message=f"No districts found for province_id {province_id}", status_code=404
            )

        return BaseResponse.success(
            message=f"Districts for province_id {province_id} retrieved successfully",
            data=districts,
        )

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)
