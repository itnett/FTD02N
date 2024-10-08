python
import matplotlib.pyplot as plt

def plot_project_timeline(tasks={"Start project": "2024-09-01", "Mid-term review": "2024-10-15", "Final presentation": "2024-12-01"}):
    """
    Plot a project timeline.
    
    Parameters:
    tasks (dict): Dictionary with task names as keys and dates as values.
    
    Returns:
    None
    """
    dates = list(tasks.values())
    task_names = list(tasks.keys())

    plt.figure(figsize=(10, 2))
    plt.plot(dates, [1]*len(dates), "ro-")
    for i, (task, date) in enumerate(tasks.items()):
        plt.text(date, 1.02, f"{task} ({date})", rotation=45, ha="right")
    plt.yticks([])
    plt.xlabel("Dates")
    plt.title("Project Timeline")
    plt.grid(True)
    plt.show()

# Example usage
plot_project_timeline()