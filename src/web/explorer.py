from fastapi import APIRouter

# prefix を設定することでパスを /explorer にする
router = APIRouter(prefix="/explorer")


@router.get("/")
def top():
    return {"message": "Hello, Explorer!"}
