import matplotlib.pyplot as plt
import math
import random

class Rabbit():
    def __init__(self, pos_x, pos_y, angle):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle

        self.speed = 0.01
        self.color = 'blue'

    def step(self):
        if random.random() < 0.2:
            self.angle += (random.random() - 0.5) * math.pi

        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        new_x, new_y = self.pos_x + dx, self.pos_y + dy

        if new_x < 0 or new_y < 0 or new_x > 1 or new_y > 1:
            self.angle += math.pi
        else:
            self.pos_x = new_x
            self.pos_y = new_y

class Fox():
    def __init__(self, pos_x, pos_y, angle):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle

        self.speed = 0.03
        self.color = 'red'

    def step(self):
        if random.random() < 0.2:
            self.angle += (random.random() - 0.5) * math.pi/2

        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        new_x, new_y = self.pos_x + dx, self.pos_y + dy

        if new_x < 0 or new_y < 0 or new_x > 1 or new_y > 1:
            self.angle += math.pi
        else:
            self.pos_x = new_x
            self.pos_y = new_y

class Experiment():
    def __init__(self, iterations, number_of_rabbits, number_of_foxes):
        self.iterations = iterations
        self.number_of_rabbits = number_of_rabbits
        self.number_of_foxes = number_of_foxes
        self.creatures= []

        self.add_rabbits(self.number_of_rabbits)
        self.add_foxes(self.number_of_foxes)
        self.setup_plot()

    def add_rabbits(self, number_of_rabbits):
        for _ in range(number_of_rabbits):
            rd_x = random.random()
            rd_y = random.random()
            rd_angle = random.random() * 2 * math.pi
            self.creatures.append(Rabbit(rd_x, rd_y, rd_angle))
    
    def add_foxes(self, number_of_foxes):
        for _ in range(number_of_foxes):
            rd_x = random.random()
            rd_y = random.random()
            rd_angle = random.random() * 2 * math.pi
            self.creatures.append(Fox(rd_x, rd_y, rd_angle))

    def run(self, iterations=None):
        if iterations == None:
            iterations = self.iterations

        for i in range(iterations):
            self.step()
            self.draw()

    def step(self):
        for r in self.creatures:
            r.step()

    def draw(self):
        self.ax1.axis([0, 1, 0, 1])

        creatures_x = [r.pos_x for r in self.creatures]
        creatures_y = [r.pos_y for r in self.creatures]
        creatures_colors = [r.color for r in self.creatures]

        self.ax1.scatter(creatures_x, creatures_y, c=creatures_colors)

        plt.draw()
        plt.pause(0.01)
        self.ax1.cla()

    def setup_plot(self):
        self.fig, self.ax1 = plt.subplots(1)
        self.ax1.set_aspect('equal')
        self.ax1.axes.get_xaxis().set_visible(False)
        self.ax1.axes.get_yaxis().set_visible(False)

if __name__ == "__main__":
    my_experiment = Experiment(100, 10, 3)
    my_experiment.run()
