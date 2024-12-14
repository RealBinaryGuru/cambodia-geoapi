from fastapi.responses import JSONResponse


class BaseResponse:
    @staticmethod
    def success(message: str = "Operation successful", data: dict = None, status_code: int = 200):
        """
        Generate a standardized success response.

        Args:
            message (str): Success message.
            data (dict): Data to include in the response.
            status_code (int): HTTP status code for the success response.

        Returns:
            JSONResponse: FastAPI JSONResponse object.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "status": "success",
                "message": message,
                "data": data or {}
            }
        )

    @staticmethod
    def error(message: str = "An error occurred", errors: dict = None, status_code: int = 400):
        """
        Generate a standardized error response.

        Args:
            message (str): Error message.
            errors (dict): Details about the errors.
            status_code (int): HTTP status code for the error response.

        Returns:
            JSONResponse: FastAPI JSONResponse object.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "status": "error",
                "message": message,
                "errors": errors or {}
            }
        )
