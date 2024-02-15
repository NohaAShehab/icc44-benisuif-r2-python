
"""
    overriding

    overloading ---->
"""
class Engineer:
    # def work(self):
    #     print("I am working")

    def work(self, no_of_hours=0):
        print(f"I am working for  {no_of_hours}")


eng = Engineer()
eng.work(88)