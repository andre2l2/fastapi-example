from fastapi import FastAPI

app = FastAPI()

class User:
  id = '1'
  user_name = 'Andre Ferreira'


@app.get('/')
def hello() -> dict[str, str]:
  return { "id": User.id, "user_name": User.user_name }

