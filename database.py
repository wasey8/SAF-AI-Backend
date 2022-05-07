from sqlalchemy import Integer, create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://nockocrboooods:429ef7fc449987d5320581ba6a7a6da86e8cbb26aa6eaefb70d7b80a8f75dfde@ec2-44-194-4-127.compute-1.amazonaws.com:5432/df5edp4tq4ep82"

db = create_engine(db_string)  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()

#User Table
class users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username=Column(String(50))
    email=Column(String(255))
    password=Column(String(255))
    
    


#base.metadata.create_all(db)
