python
# Enkel implementering av to-faktor autentisering med Python
import random

def generate_otp():
    return random.randint(100000, 999999)

def verify_otp(user_otp, generated_otp):
    return user_otp == generated_otp

generated_otp = generate_otp()
print(f"Your OTP is: {generated_otp}")

user_otp = int(input("Enter the OTP: "))
if verify_otp(user_otp, generated_otp):
    print("Access Granted")
else:
    print("Access Denied")