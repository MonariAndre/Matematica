from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Union
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Criação do app FastAPI
app = FastAPI()

# Configuração JWT
SECRET_KEY = "secret_key_exemplo"  # Substitua por uma chave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração de autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Banco de dados fictício para autenticação
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "password",  # Substitua por um hash em produção
    }
}

# Modelos
class OperationRequest(BaseModel):
    num1: float
    num2: float
    operation: str  # "add", "subtract", "multiply", "divide"

class OperationResponse(BaseModel):
    result: float

# Funções de autenticação e geração de tokens
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido ou usuário não encontrado",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )

# Endpoints
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário ou senha incorretos"
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/calculate", response_model=OperationResponse)
def calculate(op: OperationRequest, token: str = Depends(oauth2_scheme)):
    username = verify_token(token)  # Verifica e retorna o usuário autenticado
    if op.operation == "add":
        result = op.num1 + op.num2
    elif op.operation == "subtract":
        result = op.num1 - op.num2
    elif op.operation == "multiply":
        result = op.num1 * op.num2
    elif op.operation == "divide":
        if op.num2 == 0:
            raise HTTPException(status_code=400, detail="Divisão por zero não é permitida")
        result = op.num1 / op.num2
    else:
        raise HTTPException(status_code=400, detail="Operação inválida")
    return {"result": result}
