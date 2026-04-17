from pydantic import BaseModel, ConfigDict,EmailStr


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass



class EmployeeUpdate(EmployeeBase):
    pass



class EmployeeOut(EmployeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    
