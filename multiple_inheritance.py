class Father:
    def father_method(self):
        print("Father's method")

class Mother:
    def mother_method(self):
        print("Mother's method")

class Child(Father, Mother):
    def child_method(self):
        print("Child's method")

# Usage
c = Child()
c.father_method()  # From Father
c.mother_method()  # From Mother
c.child_method()   # From Child