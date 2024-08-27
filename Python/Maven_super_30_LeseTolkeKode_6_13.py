python
import tkinter as tk

class NetworkSimulationGUI:
    def __init__(self, root):
        """
        Initialiserer GUI for nettverkssimulering.
        """
        self.root = root
        self.root.title("Network Topology Simulation")

        # Oppretter tegneflate for nettverkstegning
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Tegner nettverkskomponenter
        self.draw_network()

    def draw_network(self):
        """
        Tegner komponenter og kobler dem sammen.
        """
        # Router
        self.canvas.create_rectangle(50, 250, 150, 350, fill="lightblue", outline="black")
        self.canvas.create_text(100, 300, text="Router", font=("Helvetica", 14))

        # Switch
        self.canvas.create_oval(200, 200, 300, 300, fill="lightgreen", outline="black")
        self.canvas.create_text(250, 250, text="Switch", font=("Helvetica", 14))

        # Server
        self.canvas.create_rectangle(350, 100, 450, 200, fill="lightcoral", outline="black")
        self.canvas.create_text(400, 150, text="Server", font=("Helvetica", 14))

        # Workstation 1
        self.canvas.create_rectangle(350, 300, 450, 400, fill="lightyellow", outline="black")
        self.canvas.create_text(400, 350, text="Workstation 1", font=("Helvetica", 14))

        # Workstation 2
        self.canvas.create_rectangle(500, 300, 600, 400, fill="lightyellow", outline="black")
        self.canvas.create_text(550, 350, text="Workstation 2", font=("Helvetica", 14))

        # Koble sammen komponenter
        self.canvas.create_line(150, 300, 200, 250, width=2)  # Router til Switch
        self.canvas.create_line(300, 250, 350, 150, width=2)  # Switch til Server
        self.canvas.create_line(300, 250, 350, 350, width=2)  # Switch til Workstation 1
        self.canvas

.create_line(450, 350, 500, 350, width=2)  # Workstation 1 til Workstation 2

# Hovedscriptet
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSimulationGUI(root)
    root.mainloop()