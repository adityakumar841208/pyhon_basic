class User:
    def __init__(self, name):
        self.name = name
        self.connection = []

    def addCon(self, otherUser):
        if otherUser not in self.connection:
            self.connection.append(otherUser)
            otherUser.connection.append(self)
        else : 
            print("already added connection")
        
    def showProfile(self):
        print(f"Profile:{self.name}")
        print(f"Connection:",end = "")
        for i in self.connection:
            print(i.name)


aditya = User("aditya")
ayush = User("ayush")

aditya.addCon(ayush)

print(aditya.showProfile())