
class Student:
    def __init__(self,name,major,gpa,is_on_probation):         # Attributes of the student data type
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation
# Class is like a template or the blueprint
# Object is the unique entity

    def on_honor_roll(self):
        if self.gpa>=3.5:
            return True
        else:
            return False