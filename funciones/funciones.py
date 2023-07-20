from datetime import datetime, timedelta
from jose import jwt
import hashlib

#Estas variables deberian de estar configuradas como variables de entorno
SECRETKEY = 'PRUEBAINIEN'
ALGORITH =  'HS256'


def crear_acces_token(info_user:dict):
    to_encode = info_user.copy()

    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRETKEY, algorithm=ALGORITH)
    return encoded_jwt



def generar_hash_sha256(contrasena):
    contrasena_bytes = contrasena.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(contrasena_bytes)
    hash_hexadecimal = sha256_hash.hexdigest()
    return hash_hexadecimal