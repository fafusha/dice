import matplotlib.pyplot as plt
import numpy as np

player_num = 20
avg_time = [5.129, 5.673, 6.442, 6.75725, 7.20675, 7.978, 8.7995, 9.91325, 10.483, 11.1085,
            12.90475, 13.238, 14.4525, 15.493, 17.06375, 18.68275, 18.7525, 20.81425, 22.05975]
x_val = [str(i) for i in range(2, player_num + 1)]

fig = plt.figure()
plt.yticks(np.arange(0, 25, step=1))
plt.bar(x_val, avg_time, color='grey', edgecolor = 'black')

plt.title('Average length of the round per number of players in game')
plt.xlabel('Players')
plt.ylabel('Time, minutes')


plt.show()
