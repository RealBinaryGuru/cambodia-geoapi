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


@app.get("/communes", tags=['Communes'])
def get_communes(name: str = Query(None, description="Name of the commune to search for")):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Commune.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            communes = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "district_id": row[4],
                }
                for row in csv_reader
            ]

        if name:
            communes = [
                commune for commune in communes
                if name.lower() in commune["name_en"].lower() or name.lower() in commune["name_km"].lower()
            ]

            if not communes:
                return BaseResponse.error(message="No matching communes found", status_code=404)

            return BaseResponse.success(message="Matching communes retrieved successfully", data=communes)

        return BaseResponse.success(message="Data retrieved successfully", data=communes)

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/communes/{code}", tags=['Communes'])
def get_commune_by_code(code: str):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Commune.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                if row[1] == code:
                    commune = {
                        "type": row[0],
                        "code": row[1],
                        "name_km": row[2],
                        "name_en": row[3],
                        "district_id": row[4],
                    }
                    return BaseResponse.success(message="Commune retrieved successfully", data=commune)

        return BaseResponse.error(message="Commune with the specified code not found", status_code=404)

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/communes/district/{district_id}", tags=['Communes'])
def get_communes_by_district_id(district_id: str):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Commune.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            communes = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "district_id": row[4],
                }
                for row in csv_reader
                if row[4] == district_id
            ]

        if not communes:
            return BaseResponse.error(
                message=f"No communes found for district_id {district_id}", status_code=404
            )

        return BaseResponse.success(
            message=f"Communes for district_id {district_id} retrieved successfully",
            data=communes,
        )

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


from fastapi import Query


@app.get("/villages", tags=['Villages'])
def get_paginated_villages(
        page: int = Query(1, ge=1, description="The page number to retrieve."),
        page_size: int = Query(100, ge=1, le=1000, description="Number of villages per page."),
):
    """
    Retrieve paginated villages from the dataset.
    """
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Village.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip header row

            villages = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "province_id": row[4],
                    "district_id": row[5],
                    "commune_id": row[6],
                }
                for row in csv_reader
            ]

        total_villages = len(villages)
        start = (page - 1) * page_size
        end = start + page_size

        if start >= total_villages:
            return BaseResponse.error(message="Page out of range", status_code=404)

        paginated_villages = villages[start:end]

        return BaseResponse.success(
            message="Paginated villages retrieved successfully",
            data={
                "page": page,
                "page_size": page_size,
                "total": total_villages,
                "villages": paginated_villages,
            },
        )

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/villages/search", tags=['Villages'])
def search_villages_by_name(
        name: str = Query(..., description="Name of the village to search for (in English or Khmer)."),
        page: int = Query(1, ge=1, description="The page number to retrieve."),
        page_size: int = Query(100, ge=1, le=1000, description="Number of villages per page."),
):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Village.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)

            matching_villages = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "province_id": row[4],
                    "district_id": row[5],
                    "commune_id": row[6],
                }
                for row in csv_reader
                if name.lower() in row[2].lower() or name.lower() in row[3].lower()
            ]

        total_villages = len(matching_villages)
        start = (page - 1) * page_size
        end = start + page_size

        if not matching_villages:
            return BaseResponse.error(message="No villages found matching the search term", status_code=404)

        paginated_villages = matching_villages[start:end]

        return BaseResponse.success(
            message="Matching villages retrieved successfully",
            data={
                "page": page,
                "page_size": page_size,
                "total": total_villages,
                "villages": paginated_villages,
            },
        )

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)


@app.get("/villages/commune/{commune_id}", tags=['Villages'])
def get_villages_by_commune_id(
        commune_id: str,
        page: int = Query(1, ge=1, description="The page number to retrieve."),
        page_size: int = Query(100, ge=1, le=1000, description="Number of villages per page."),
):
    current_dir = Path(__file__).parent
    file_path = current_dir / "data" / "Village.csv"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            villages = [
                {
                    "type": row[0],
                    "code": row[1],
                    "name_km": row[2],
                    "name_en": row[3],
                    "province_id": row[4],
                    "district_id": row[5],
                    "commune_id": row[6],
                }
                for row in csv_reader
                if row[6] == commune_id
            ]

        total_villages = len(villages)
        start = (page - 1) * page_size
        end = start + page_size

        if not villages:
            return BaseResponse.error(
                message=f"No villages found for commune_id {commune_id}",
                status_code=404
            )

        paginated_villages = villages[start:end]

        return BaseResponse.success(
            message=f"Villages for commune_id {commune_id} retrieved successfully",
            data={
                "page": page,
                "page_size": page_size,
                "total": total_villages,
                "villages": paginated_villages,
            },
        )

    except Exception as e:
        return BaseResponse.error(message=f"An unexpected error occurred: {str(e)}", status_code=500)
