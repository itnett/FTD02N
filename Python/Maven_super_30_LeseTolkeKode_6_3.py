python
import tkinter as tk

class NetworkSimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Topology Simulation")

        # Create canvas for drawing
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

        # Draw LAN components
        self.draw_network()

    def draw_network(self):
        # Drawing LAN components
        self.canvas.create_rectangle(50, 150, 150, 250, fill="lightblue", outline="black")
        self.canvas.create_text(100, 200, text="Router", font=("Helvetica", 14))

        self.canvas.create_oval(200, 100, 300, 200, fill="lightgreen", outline="black")
        self.canvas.create_text(250, 150, text="Switch", font=("Helvetica", 14))

        self.canvas.create_rectangle(350, 50, 450, 150, fill="lightcoral", outline="black")
        self.canvas.create_text(400, 100, text="Server", font=("Helvetica", 14))

        self.canvas.create_rectangle(350, 250, 450, 350, fill="lightyellow", outline="black")
        self.canvas.create_text(400, 300, text="Workstation", font=("Helvetica", 14))

        # Connect components with lines
        self.canvas.create_line(150, 200, 200, 150, width=2)  # Router to Switch
        self.canvas.create_line(300, 150, 350, 100, width=2)  # Switch to Server
        self.canvas.create_line(300, 150, 350, 300, width=2)  # Switch to Workstation

# Main script
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSimulationGUI(root)
    root.mainloop()