
class User():

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_email(cls, email):
        name = email.split(".")[0]
        return cls(name)
    
a = User.from_email("aaa.aaa@h.com")

print(a.name)

