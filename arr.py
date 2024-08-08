import random as rd
import matplotlib.pyplot as plt


otp_array = [] # OTP Array آبرودی جان پرش کن
id_array = [] # ID Array آبرودی جان پرش کن
plt.figure(figsize=(12, 6))  # Set the figure size for better visibility
plt.scatter(y=otp_array, x=id_array, color='skyblue', edgecolor='black')
plt.title('Distribution of Random Numbers Between 1000 and 9999')
plt.xlabel('Random Number Value')
plt.ylabel('Frequency')
plt.show()