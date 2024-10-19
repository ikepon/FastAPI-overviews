from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter

basic = HTTPBasic()


@router.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)):
    return {"username": creds.username, "password": creds.password}
