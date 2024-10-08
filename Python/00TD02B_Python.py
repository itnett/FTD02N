python
def write_technical_report(title="Technical Report on AI", author="Jane Smith", content="This report discusses the applications of AI in various fields."):
    """
    Write a technical report.
    
    Parameters:
    title (str): Title of the report.
    author (str): Author of the report.
    content (str): Content of the report.
    
    Returns:
    str: Technical report.
    """
    report = (
        f"Title: {title}\n"
        f"Author: {author}\n\n"
        f"Abstract:\n"
        f"{content[:150]}...\n\n"
        f"Content:\n"
        f"{content}\n"
    )
    print(report)
    return report

# Example usage
write_technical_report()