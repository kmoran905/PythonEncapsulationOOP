from collections import namedtuple
from dataclasses import dataclass

##This demonstrates encapsulation.

##I was trying out namedtuple in the beginning of this excerise but I found that dataclass was better for OOP Encapsulation
## Profile = namedtuple('Profile' , 'name, age , location')


##Without data class
##class Profile():
  ##  def __init__(self , name , age , location) -> None:
    ##    self.name = name
      ##  self.age = age
        ##self.location = location
        
    ## def __repr__(self) -> str:
       ## return "{}\n{}\n{}\n".format(self.name , self.age , self.location)
       
       
## Using dataclass     
@dataclass
class Profile:
    name: str
    age: int
    location: str

    # __repr__ is the object representation in string forma
    def __repr__(self) -> str:
        return "{}\n{}\n{}\n".format(self.name , self.age , self.location)
               
profile1 = Profile("James" , 34 , "New Zealand")
profile2 = Profile("Rachel" , 40 , "United States of America")
print(profile1)
print(profile2)
