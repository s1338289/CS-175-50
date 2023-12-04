#Victor Davidson
#CS 175-50
#expenses.txt

import matplotlib.pyplot as plt

expense = ["1000", "250", "300", "200", "375", "800"]
category = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Other"]
f =open("expense.txt", "r")
f.writelines(category)
f.writelines(expense)
f.readlines()
f.readlines()
plt.pie (expense, labels = category, startangle = 90, autopct = '%.1f%%')
plt.title ('Monthly Expense Pie Chart')
plt.show()
f.close ()
