from typing import Optional
from typing import Dict
from pydantic import BaseModel
from datetime import date

today = date.today()
class FilesInDB(BaseModel): 
    #Atributos de la clase
    #La clase BaseModel ya tiene un constructor
    nombre: str
    tipo: str
    peso: int
    fecha_Carga: Optional[str]
database_files = Dict[str, FilesInDB]
database_files = {
    "Contabilidad": FilesInDB(**{"nombre":"Contabilidad", #Los asteriscos sirven para indicar que van argumentos pero aun no se saben cuantos
                            "tipo":"XLSX",
                            "peso":12000,
                            "fecha_Carga": today.strftime("%d/%m/%Y")}),
    "Acta": FilesInDB(**{"nombre":"Acta",
                            "tipo":"PDF",
                            "peso":1100,
                            "fecha_Carga": today.strftime("%d/%m/%Y")}),
}
