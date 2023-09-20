def Power(number, exponent):
    print(num ** exponent)

class Map:
    def __init__(self):
        self.map = [['t', 't', 'g', 'm', 'w'], 
        ['t', 'g', 'g', 'w', 'w'],
        ['t', 'g', 'g', 'w', 'w'],
        ['t', 'g', 'g', 'w', 'w'],
        ['t', 'g', 'g', 'w', 'w']]
        self.x = 2
        self.y = 2

    def __str__(self):
        return str(self.map)

m = Map()

class Game():
    def __init__(self):
        self.theMap = Map()

    def run(self):
        while True:
            location = self.theMap.map[self.theMap.y][self.theMap.x]
            if location == 'm':
                print("you are in a mountain")
            elif location == 'g':
                print("you are in a grassy meadow")
            elif location == 't':
                print("you are in a forest")
            elif location == 'w':
                print("you are swimming in water")

            answer = input("What do you want to do?")
            if (answer == 'q'):
                break;
            elif (answer == 'w'):
                self.theMap.y += 1
            elif (answer == 'a'):
                self.theMap.x -= 1
            elif (answer == 's'):
                self.theMap.y -= 1
            elif (answer == 'd'):
                self.theMap.x += 1
            else:
                print("I don't understand.")

game = Game()


