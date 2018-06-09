import matplotlib
matplotlib.use("TKAgg")

from matplotlib import pyplot

# label, value for pie chart

# 1 Prepare data
labels = ["iOS", "Android", "Web", "React Native"]
values = [20, 15, 40, 25]
colors = ['red', 'green', 'gold', 'purple']
explode = [0, 0, 0, 0.2]


# 2 Plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode, shadow = True)
pyplot.axis('equal')
# 3 Show
pyplot.show()


