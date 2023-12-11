import tkinter as tk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.root.geometry("800x600")

        self.data = [random.randint(1, 1000) for _ in range(100)]
        self.canvas = tk.Canvas(self.root, height=400, width=800, bg="white")
        self.canvas.pack(pady=20)

        self.sort_button = tk.Button(self.root, text="Start Sorting", command=self.bubble_sort)
        self.sort_button.pack()

    def draw_bars(self):
        self.canvas.delete("all")
        bar_width = 8
        for i, value in enumerate(self.data):
            x1 = i * (bar_width + 2)
            y1 = 400
            x2 = x1 + bar_width
            y2 = 400 - value * 0.4
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

        self.root.update_idletasks()
        time.sleep(0.05)

    def bubble_sort(self):
        n = len(self.data)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    self.draw_bars()  # Draw bars after swapping

        self.draw_bars()

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
