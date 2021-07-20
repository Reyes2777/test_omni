from starlette.responses import JSONResponse


def response(message: str, status_code: int, data=None):
    data_response = {
        "message": message,
        "status_code": status_code
    }
    if data:
        data_response['data'] = data
    return JSONResponse(data_response, status_code=status_code)