from pydantic import BaseModel , Field
from typing import Optional

class Employee(BaseModel):
    id: int = Field(...,gt = 0, description = "The ID must be a positive integer", example = 1, title = "Employee ID")
    name: str =Field(..., min_length = 3, max_length= 20, description = "The name must be between 3 and 20 characters", example = "John Doe", title = "Employee Name")
    age: int = Field(..., gt= 18, lt = 65, description = "The age must be between 18 and 65", example = 30, title = "Employee Age")
    department: str = Field(..., min_length = 2, max_length = 20, description = "The department must be between 3 and 20 characters", example = "HR", title = "Employee Department")
    series: Optional[int] = Field(None, gt = 0, description = "The series must be a positive integer", example = 1, title = "Employee Series")