import matplotlib.pyplot as plt
import math
import random


class Creature():
    def __init__(self, pos_x, pos_y, angle):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle

        self.alive = True
        self.speed = 0.01
        self.color = 'black'

    def step(self):
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        new_x, new_y = self.pos_x + dx, self.pos_y + dy

        if new_x < 0 or new_y < 0 or new_x > 1 or new_y > 1:
            self.angle += math.pi
        else:
            self.pos_x = new_x
            self.pos_y = new_y

    def distance(self, other):
        return math.sqrt((self.pos_x - other.pos_x)**2
                         + (self.pos_y - other.pos_y)**2)

    def interact(self, other):
        pass


class Rabbit(Creature):
    def __init__(self, pos_x, pos_y, angle):
        super().__init__(pos_x, pos_y, angle)

        self.speed = 0.01
        self.color = 'blue'

    def step(self):
        if random.random() < 0.2:
            self.angle += (random.random() - 0.5) * math.pi

        super().step()


class Fox(Creature):
    def __init__(self, pos_x, pos_y, angle):
        super().__init__(pos_x, pos_y, angle)

        self.hunger = 0
        self.speed = 0.03
        self.color = 'red'

    def step(self):
        if self.hunger >= 80:
            self.alive = False
        self.hunger += 1

        if random.random() < 0.2:
            self.angle += (random.random() - 0.5) * math.pi/2

        super().step()

    def interact(self, other):
        super().interact(other)
        if type(other) is Rabbit:
            other.alive = False
            self.hunger = 0


class Experiment():
    def __init__(self, iterations, number_of_rabbits, number_of_foxes):
        self.iterations = iterations
        self.number_of_rabbits = number_of_rabbits
        self.number_of_foxes = number_of_foxes
        self.creatures = []

        self.add_rabbits(self.number_of_rabbits)
        self.add_foxes(self.number_of_foxes)
        self.interaction_distance = 0.05
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

    def resolve_deaths(self):
        for i in reversed(range(len(self.creatures))):
            if not self.creatures[i].alive:
                self.creatures.pop(i)

    def run(self, iterations=None):
        if iterations is None:
            iterations = self.iterations

        for i in range(iterations):
            self.step()
            self.draw()

    def step(self):
        for r in self.creatures:
            r.step()
        self.handle_interaction()
        self.resolve_deaths()

    def draw(self):
        self.ax1.axis([0, 1, 0, 1])

        creatures_x = [r.pos_x for r in self.creatures]
        creatures_y = [r.pos_y for r in self.creatures]
        creatures_colors = [r.color for r in self.creatures]

        self.ax1.scatter(creatures_x, creatures_y, c=creatures_colors)

        plt.draw()
        plt.pause(0.03)
        self.ax1.cla()

    def setup_plot(self):
        self.fig, self.ax1 = plt.subplots(1)
        self.ax1.set_aspect('equal')
        self.ax1.axes.get_xaxis().set_visible(False)
        self.ax1.axes.get_yaxis().set_visible(False)

    def handle_interaction(self):
        for creature1 in self.creatures:
            for creature2 in self.creatures:
                if creature1 is not creature2 and creature1.distance(creature2) < self.interaction_distance:
                    creature1.interact(creature2)


if __name__ == "__main__":
    my_experiment = Experiment(100, 20, 4)
    my_experiment.run()
