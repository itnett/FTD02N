python
    from datetime import datetime

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 6, 30)
    today = datetime.today()

    project_duration = (end_date - start_date).days
    days_elapsed = (today - start_date).days
    progress = (days_elapsed / project_duration) * 100

    print(f"Prosjektfremdrift: {progress:.1f}%")