from fastapi import APIRouter

router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return {"message": "Dado criado com sucesso"}

@router.post("file/add_data")
async def add_data():
    return {"message": "Dado adicionado com sucesso"}

@router.delete("/file/delete_data")
async def delete_data():
    return {"message": "Dado removido com sucesso"}

@router.delete("/file/List_files")
async def list_data():
    return {"message": "Lista de dados"}