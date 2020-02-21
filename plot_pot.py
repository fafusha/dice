import matplotlib.pyplot as plt
import numpy as np

player_num = 20
avg_pot = [0.1062, 0.1698, 0.2392, 0.3115, 0.3897, 0.48615, 0.602, 0.7240, 0.827,
           0.969, 1.155, 1.3039, 1.4595, 1.635, 1.9, 2.2423, 2.3067, 2.66665, 2.935]
x_val = [str(i) for i in range(2, player_num + 1)]

fig = plt.figure()
plt.yticks(np.arange(0, 5, step=0.5))
plt.bar(x_val, avg_pot, color='grey', edgecolor = 'black')

plt.title('Average size of the winning pot per number of players in the game')
plt.xlabel('Players')
plt.ylabel('Winning Pot, Dollars')


plt.show()
