class rooms:
    def __init__(self,roomname):
        self.roomname=roomname


class house:
    def __init__(self, name,room1,room2,room3):
        self.name = name
        self.roomname1=room1
        self.roomname2=room2
        self.roomname3=room3


        self.room1=rooms(room1)
        self.room2=rooms(room2)
        self.room3=rooms(room3)
    def show(self):
        return print("House name is", self.name,"and it has rooms with names",
            self.roomname1, self.roomname2, self.roomname3)



p = house("housename", "sauna", "livingroom", "kitchen")

p.show()
