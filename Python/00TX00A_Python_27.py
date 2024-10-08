python
def create_budget(revenue_items={'Product Sales': 50000, 'Service Revenue': 20000}, expense_items={'Rent': 10000, 'Salaries': 25000, 'Utilities': 3000, 'Marketing': 5000}):
    """
    Create a budget based on revenue and expense items.
    
    Parameters:
    revenue_items (dict): Dictionary of revenue items with their values.
    expense_items (dict): Dictionary of expense items with their values.
    
    Returns:
    pd.DataFrame: Budget dataframe.
    """
    revenue_df = pd.DataFrame(list(revenue_items.items()), columns=['Item', 'Amount'])
    revenue_df['Type'] = 'Revenue'
    
    expense_df = pd.DataFrame(list(expense_items.items()), columns=['Item', 'Amount'])
    expense_df['Type'] = 'Expense'
    
    budget_df = pd.concat([revenue_df, expense_df])
    
    total_revenue = revenue_df['Amount'].sum()
    total_expense = expense_df['Amount'].sum()
    net_income = total_revenue - total_expense
    
    budget_summary = pd.DataFrame({'Item': ['Total Revenue', 'Total Expenses', 'Net Income'], 'Amount': [total_revenue, total_expense, net_income], 'Type': ['Summary', 'Summary', 'Summary']})
    
    budget_df = pd.concat([budget_df, budget_summary])
    
    display(budget_df)
    return budget_df

# Eksempel på bruk
create_budget()