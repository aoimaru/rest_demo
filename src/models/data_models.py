
class Student(Base):
    __tablename__ = 'students'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
 

class StudentSchema(ModelSchema):
    class Meta:
        model = Student
 
