from fastapi import FastAPI, Request, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app import crud
from app.db import get_db


app = FastAPI()

# endpoint: GET /healthz
@app.get("/healthz")
def health_check(request: Request, db: Session = Depends(get_db)):
    #  if query params or body return 400
    if request.query_params or request.headers.get("content-length") not in (None, "0"):
        return Response(
            status_code=status.HTTP_400_BAD_REQUEST,
            headers={"Cache-Control": "no-cache"},
            content=b""
        )

    try:
        
        crud.create_health_check(db)

        # Return 200 OK empty body
        return Response(
            status_code=status.HTTP_200_OK,
            headers={"Cache-Control": "no-cache"},
            content=b""
        )
    except Exception:
        # Database failed 
        return Response(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            headers={"Cache-Control": "no-cache"},
            content=b""
        )


@app.post("/healthz")
@app.put("/healthz")
@app.delete("/healthz")
@app.patch("/healthz")
def method_not_allowed():
    return Response(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        headers={"Cache-Control": "no-cache"},
        content=b""
    )
