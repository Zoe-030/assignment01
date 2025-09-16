from fastapi import FastAPI, Request, Depends, status
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db

app = FastAPI()

@app.get("/healthz")
def health_check(request: Request, db: Session = Depends(get_db)):
   
    if request.query_params or request.headers.get("content-length") not in (None, "0"):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Request must not contain query params or body"}
        )

    try:
        
        crud.create_health_check(db)

        
        return Response(
            status_code=status.HTTP_200_OK,
            headers={"Cache-Control": "no-cache"},
            content=b""
        )
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"error": "Service unavailable"}
        )
