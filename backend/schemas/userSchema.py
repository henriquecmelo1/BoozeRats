from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    points: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        from_attributes = True
