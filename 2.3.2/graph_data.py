import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.00398206710815,0.0208818912506, 0.16832280159, 1.69691109657] 
B_time = [0.00746703147888,0.00282096862793, 0.00282406806946, 0.00280785560608, 0.00285482406616, 0.00282597541809, 0.00280785560608, 0.0028169155120]

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algorithm A') # red dotsquit
ax.plot(B_input_chars, B_time, 'bo-',label='Algorithm B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Worst case execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left')
ax.margins(.1)
fig.set_facecolor('white')
fig.savefig('graph1_data')
