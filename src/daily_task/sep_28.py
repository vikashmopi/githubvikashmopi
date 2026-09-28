from pydantic import BaseModel #BaseModel = the form checker.

class person(BaseModel):
    name:str
    age:int
    email:str

valide_data=person(name="vikash123",age="22",email="vikashhravi05@gmail.com")
print(valide_data)