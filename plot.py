import matplotlib.pyplot as plt


def show():
    plt.show()


class Plot:
    def __init__(self, data):
        self.data = data
        self.comparisons = 0
        self.fig, self.ax = plt.subplots()

    def update(self, highlight):
        self.comparisons += 1

        x = list(range(len(self.data)))
        colors = ['r' if i == highlight else 'b' for i in range(len(self.data))]

        self.ax.clear()
        self.ax.bar(x, self.data, color=colors)
        self.ax.set_title("Sort is processing...")
        self.ax.set_xlabel('Size')
        self.ax.set_ylabel('Data Value')
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(x)

        plt.pause(0.1)

