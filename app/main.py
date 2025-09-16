from fastapi import FastAPI, Request, Depends, status
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db

# This is the main entry point of app 
app = FastAPI()

# This is only endpoint
@app.get("/healthz")
def health_check(request: Request, db: Session = Depends(get_db)):
    # If the request has query parameters (?foo=bar) Or has a body (data), return 400 
    if request.query_params or request.headers.get("content-length") not in (None, "0"):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Request must not contain query params or body"}
        )

    try:
        # insert a new health check record into the database
        crud.create_health_record(db)

        # If it worked, return 200 OK
    
        return Response(
            status_code=status.HTTP_200_OK,
            headers={"Cache-Control": "no-cache"},
            content=b""
        )
    except Exception:
        # If the DB insert failed,return 503 (Service Unavailable)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"error": "Service unavailable"}
        )
