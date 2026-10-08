from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

def validate_user_data(user_id: int, user_name: str) -> str:
    user = User(id=user_id, name=user_name)
    return f"Валідація пройшла успішно: {user.name} (ID: {user.id})"