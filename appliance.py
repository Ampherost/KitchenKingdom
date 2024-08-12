class Appliance:
    def __init__(self, name, capacity, speed):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.in_use = False

    def start(self, ingredients):
        if not self.in_use:
            self.in_use = True
            # Start cooking logic
            print(f"{self.name} started with {ingredients}")

    def stop(self):
        self.in_use = False
        print(f"{self.name} is now free")
