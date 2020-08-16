import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        self.balls = balls
        for k,v in self.balls.items():
            for val in range(v):
                self.contents.append(k)


    def draw(self, remove):
        self.remove = remove
        rando_list = []

        if  remove <= len(self.contents):
            for i in range(remove):
                rando = random.choice(self.contents) #chooses random element in list from specified hat
                rando_list.append(rando)
                self.contents.remove(rando)

            return rando_list
        else:
            return self.contents



def experiment(**kwargs):

    expected_balls_list = {}
    copyhat = ''
    drawballs = 0
    experiment = 0
    M = 0
    for k,v in kwargs.items():

        if k == 'hat':
            copyhat = copy.deepcopy(v) #adds a copy of the of choosen hat object to varialbe inside function // can use functions inside copied class as well

        elif k == 'expected_balls':
            expected_balls_list = v

        elif k == 'num_balls_drawn':
            drawballs = v

        elif k == 'num_experiments':
            experiment = v


    for i in range(experiment):
        drawn = {}
        count = 0
        match = len(expected_balls_list)
        exhat = copy.deepcopy(copyhat)


        for ball in exhat.draw(drawballs):
            drawn[ball] = drawn.get(ball,0) + 1 #adds drawn balls to dictionary and if they are already in dict, increase value by 1

        for key, value in drawn.items():
            #comparing to see if in from dranw items is in the expected ball list and it is, check if it's vaule is equal or greater than the expected list value
            if key in expected_balls_list and value >= expected_balls_list.get(key,value):
                count += 1

        if count == match:
            M += 1

    return M / experiment





###########tests#######

#hat = Hat(black=6, red=4, green=3)
hat = Hat(blue=3,red=2,green=6)
#print(experiemnt(hat=hat, 2))
#print(experiemnt(hat=hat,
#                 expected_balls={"red":2,"green":1},
#                 num_balls_drawn=5,
#                 num_experiments=2000))


print(experiment(hat=hat,
                 expected_balls={"blue":2,"green":1},
                 num_balls_drawn=4,
                 num_experiments=1000))

