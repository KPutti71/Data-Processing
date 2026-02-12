import matplotlib.pyplot as plt
import math

class Rabbit():
    # TODO define rabbit

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
