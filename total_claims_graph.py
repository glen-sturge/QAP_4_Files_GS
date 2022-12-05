# QAP 4: A program that will allow the user to enter the total amount of claims for each
# month from January to December and then display it to a linegraph using the matplotlib module.
# Author: Glen Sturge       Date: 12/04/2022

import matplotlib.pyplot as plt

# Define font
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = []

for month in range(0, 12):
    while True:
        try:
            claim_qty = float(input(f"Enter the claims dollar value total for {x_axis[month]} : $ "))
        except ValueError:
            print("That wasn't a number! Try again.")
        else:
            break
    y_axis.append(claim_qty)


plt.plot(x_axis, y_axis, 'go--', linewidth=2, markersize=12)
plt.title("Total Monthly Claims", fontdict=font)
plt.xlabel("Month", fontdict=font)
plt.ylabel("Claims Value ($)", fontdict=font)
plt.show()
