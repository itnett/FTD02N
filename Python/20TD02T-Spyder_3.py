python
   def visualize_data():
       query = '''
       SELECT Users.username, Orders.product, Orders.amount
       FROM Users
       JOIN Orders ON Users.user_id = Orders.user_id
       '''
       df = pd.read_sql_query(query, conn)

       df.groupby('username').sum()['amount'].plot(kind='bar')
       plt.title('Total Orders by User')
       plt.xlabel('User')
       plt.ylabel('Total Orders')
       plt.show()