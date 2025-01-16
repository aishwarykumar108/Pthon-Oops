#initiate a class
class employee:
    #special method/magic methhod/dunder method - constructor
    def __init__(self):
        print("Started executing attribute/data")
        self.id = 1234
        self.salary = 95000
        self.designation = 'SDE'
        self.name = 'Aishwary'
        print("attribute/data have been executing ")
    
    def travel(self,destination):
        print(self.name,"Traveling toward's ",destination)

#creating a object / instance of the class 
emp =employee()

print(emp.name)
emp.travel("Delhi")