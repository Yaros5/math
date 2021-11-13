import matplotlib.pyplot as plt


list_1 = list(range(-1000, 1000))
list_2 = []
plt.style.use('seaborn')
for x in range(-1000, 1000):
    res = x ** 2
    list_2.append(res)
fig, ax = plt.subplots()
ax.plot(list_1, list_2, c = (0.1, 0.4, .03))
plt.show()
