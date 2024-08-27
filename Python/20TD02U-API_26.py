python
import requests

def get_user_orders(user_id):
    user = requests.get(f'http://localhost:5000/users/{user_id}').json()
    orders = requests.get(f'http://localhost:5001/orders?user_id={user_id}').json()
    return {'user': user, 'orders': orders}

if __name__ == '__main__':
    user_orders = get_user_orders(1)
    print(user_orders)