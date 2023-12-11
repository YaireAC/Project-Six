import tkinter as tk
import time
import random

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorter")
        self.root.geometry("600x400")

        self.values = random.sample(range(1, 101), 10)  
        self.rectangles = []

        self.canvas = tk.Canvas(self.root, width=600, height=300, bg="white")
        self.canvas.pack()

        self.sort_button = tk.Button(self.root, text="Start Sorting", command=self.bubble_sort)
        self.sort_button.pack()

    def draw_rectangles(self, highlighted=None):
        self.canvas.delete("all")

        rectangle_width = 50
        for i, value in enumerate(self.values):
            x1 = i * rectangle_width
            x2 = (i + 1) * rectangle_width
            y1 = 300 - value * 3  
            y2 = 300

            color = "lightblue" if i in highlighted else "blue"
            self.rectangles.append(self.canvas.create_rectangle(x1, y1, x2, y2, fill=color))

        self.root.update()
        time.sleep(0.5)  

    def swap_values(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]

    def bubble_sort(self):
        n = len(self.values)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.draw_rectangles([j, j + 1])  
                if self.values[j] > self.values[j + 1]:
                    self.swap_values(j, j + 1)
                    self.draw_rectangles([j, j + 1])  

        self.draw_rectangles(range(len(self.values)))

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
