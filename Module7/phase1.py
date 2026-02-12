import matplotlib.pyplot as plt
import math

class Rabbit():
    def __init__(self, pos_x, pos_y, angle):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle

        self.speed = 0.01
        self.color = 'blue'

    def step(self):
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        new_x, new_y = self.pos_x + dx, self.pos_y + dy

        if new_x < 0 or new_y < 0 or new_x > 1 or new_y > 1:
            self.angle += math.pi
        else:
            self.pos_x = new_x
            self.pos_y = new_y

class Experiment():
    def __init__(self, iterations, rabbit):
        self.iterations = iterations
        self.rabbit = rabbit
        
        self.setup_plot()

    def run(self, iterations=None):
        if iterations == None:
            iterations = self.iterations

        for i in range(iterations):
            self.step()
            self.draw()

    def step(self):
        self.rabbit.step()

    def draw(self):
        self.ax1.axis([0, 1, 0, 1])

        self.ax1.scatter(self.rabbit.pos_x, self.rabbit.pos_y)
        # TODO plot rabbit

        plt.draw()
        plt.pause(0.01)
        self.ax1.cla()

    def setup_plot(self):
        self.fig, self.ax1 = plt.subplots(1)
        self.ax1.set_aspect('equal')
        self.ax1.axes.get_xaxis().set_visible(False)
        self.ax1.axes.get_yaxis().set_visible(False)

if __name__ == "__main__":
    my_rabbit = Rabbit(0.25, 0.75, math.pi/4)
    my_experiment = Experiment(100, my_rabbit)
    my_experiment.run()
