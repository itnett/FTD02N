python
def fetch_data():
    users_data = pd.read_sql_query("SELECT * FROM Users", conn)
    orders_data = pd.read_sql_query("SELECT * FROM Orders", conn)
    print("Users Data:")
    print(users_data)
    print("\nOrders Data:")
    print(orders_data)

fetch_data()