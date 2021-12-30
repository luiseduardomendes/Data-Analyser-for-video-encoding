from matplotlib import pyplot as plt

dev_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dev_y = [34, 32, 59, 13, 15, 96, 79, 90, 64, 21].sort()

#changing plot stile
plt.style.use('ggplot')

devy2 = [91, 74, 89, 57, 18, 25, 67, 40, 38, 59]

# creating plot and name of curves
plt.plot(dev_x, dev_y, label='Crescent')
plt.plot(dev_x, devy2, label='Random')

# format https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# creating legend
plt.legend()

# creating title and axis names
plt.title('matplotlib tests')
plt.xlabel('x axis')
plt.ylabel('y axis')

# enable grid
plt.grid(True)

#plt.tight_layout()

# saving image
plt.savefig('plot.png')

# showing plot in png
plt.show()