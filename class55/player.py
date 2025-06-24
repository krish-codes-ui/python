class Player():
    def __init__(self,name):
        self.health = 100
        self.level = 1
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def attack(self):
        print(f"{self.name} is attacking.")

    def walk(self):
        print(f"{self.name} is walking.")

