from pydantic import BaseModel


class NewUser(BaseModel):
    new_user_id: int
    new_user_name: str
    new_password: str
    new_user_email: str
