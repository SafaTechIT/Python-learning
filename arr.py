import random as rd
import matplotlib.pyplot as plt


random_numbers = [rd.randint(1, 100000) for _ in range(10000)]
plt.figure(figsize=(12, 6))  # Set the figure size for better visibility
plt.hist(random_numbers, bins=100, color='skyblue', edgecolor='black')
plt.title('Distribution of Random Numbers Between 1 and 100000')
plt.xlabel('Random Number Value')
plt.ylabel('Frequency')