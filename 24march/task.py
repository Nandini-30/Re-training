from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import  sqlite

Base =declarative_base()

class Task(Base):
    __tablename__= "people" # table name
    ssn=Column("ssn",Integer,primary_key=True)
    firstname=Column("firstname",String)
    lastname=Column("lastname",String)
    gender=Column("gender",CHAR)
    age=Column("age",Integer)

    def __init__(self,ssn,firstname,lastname,gender,age): 
        self.ssn=ssn
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.age=age

    def __repr__(self):
        return f"{self.ssn} --{self.firstname} --{self.lastname}--{self.gender}--{self.age}"
    
class Thing(Base):
    __tablename__="things"
    tid=Column("tid",Integer,primary_key=True)
    description=Column("description",String)
    owner=Column("ssn",Integer,ForeignKey(Task.ssn))

    def __init__(self,tid,description,owner):
        self.tid=tid
        self.description=description
        self.owner=owner

    def __repr__(self):
        return f"{self.tid}  --{self.description} -- {self.owner}"

        
        
def poc():
 
    engine =create_engine("sqlite:///freak.db",echo=True)#rituals
    Base.metadata.create_all(bind=engine)#create tables
    Session=sessionmaker(bind=engine)#create the class
    session=Session()#object creation
    
    #task=session.query(task).get(1)
    #task.age=11
    #session.commit()

    results = session.query(Thing,Task).filter(Thing.owner ==Task.ssn)
    for r in results:
        print(r)

poc();



