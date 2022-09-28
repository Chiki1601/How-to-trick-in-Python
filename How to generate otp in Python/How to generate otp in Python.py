import random

otp_length = 12
numbers = '1234567890'
otp = ""

for index in range(otp_length):
    otp = otp + random.choice(numbers)

print("otp generated: {}".format(otp))
