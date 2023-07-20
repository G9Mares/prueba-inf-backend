from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from funciones.dbconexion import sql_instance
from funciones.funciones import crear_acces_token , generar_hash_sha256
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre:str
    telefono:str
    correo:str
    password:str




router = APIRouter()

@router.post('/login')
async def login(form:OAuth2PasswordRequestForm =Depends()):
    usuario = sql_instance.usuario_info_by_nombre(form.username)
    if not usuario:
        raise HTTPException(status_code=404,detail="Datos de acceso invalidos")
    if usuario.nombre == 'admin' and usuario.password == form.password:
        acces_token = crear_acces_token({"user":usuario.nombre,"id":usuario.id})
        return {"access_token":acces_token,"token_type":"bearer",'session':{'id':usuario.id,'username':usuario.nombre,'email':usuario.correo,'tel':usuario.tel}}
    passhash = generar_hash_sha256(form.password)
    print(passhash)
    if passhash == usuario.password:
        acces_token = crear_acces_token({"user":usuario.nombre,"id":usuario.id})
        return {"access_token":acces_token,"token_type":"bearer",'session':{'id':usuario.id,'username':usuario.nombre,'email':usuario.correo,'tel':usuario.tel}}    
    raise HTTPException(status_code=404,detail="Datos de acceso invalidos")

@router.post('/registro')
async def registro(user:Usuario):
    passhash = generar_hash_sha256(user.password)
    print(passhash)
    crear_user = sql_instance.crear_usuario(user.nombre, user.correo, user.telefono,passhash)
    if crear_user:
        return {'message':"Usuario creado con exito",'status':'success'}
    raise HTTPException(status_code=409, detail='Ya existe un usario con ese nombre o correo')    


    
    