from pydantic import BaseModel
from fastapi import FastAPI
from datetime import date
from fastapi import HTTPException
from db.files_db import database_files
from db.files_db import FilesInDB


#from image.user_db import UserInDB
#  uvicorn main:app --reload

app = FastAPI()
today = date.today()

@app.get("/files")
async def files():
    #return {"message": database_files.get("Contabilidad")}
    return {"message": database_files}

@app.get("/files/{file}")
async def users_by_user(file : str):
    if file in database_files:
        return {"message": database_files[file]} #Se usa la variable user enviada en el get para buscar un archivo
    else:
        raise HTTPException(status_code=404,detail="El archivo no existe en la base de Datos")

@app.post("/upload")
async def upload(file : FilesInDB):
    file.fecha_Carga=today.strftime("%d/%m/%Y")
    database_files[file.nombre] = file
    return file

