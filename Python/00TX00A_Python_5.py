python
def create_marketing_plan(objectives=["Increase brand awareness", "Generate leads"], budget=5000, channels=["Social Media", "Email Marketing", "SEO"]):
    """
    Create a marketing plan.
    
    Parameters:
    objectives (list): List of marketing objectives.
    budget (int): Budget for the marketing plan.
    channels (list): List of marketing channels.
    
    Returns:
    dict: Marketing plan.
    """
    plan = {
        "Objectives": objectives,
        "Budget": budget,
        "Channels": channels
    }
    
    print("Marketing Plan:")
    print(f"Objectives: {', '.join(objectives)}")
    print(f"Budget: ${budget}")
    print(f"Channels: {', '.join(channels)}")
    
    return plan

# Example usage
create_marketing_plan()