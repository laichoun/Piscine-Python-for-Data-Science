# class A:
#     def __init__(self):
#         super().__init__()
#         print("A init")

# class B:
#     def __init__(self):
#         super().__init__()
#         print("B init")

# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("C init")

# c = C()


class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C init")
        

c = C()