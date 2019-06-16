import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.00406694412231,0.0221271514893, 0.166985034943, 1.98512983322] 
B_time = [0.00839400291443, 0.00967907905579, 0.012845993042, 0.0238311290741, 0.0578210353851, 0.177696943283, 0.561136007309, 1.6988298893] 

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algo. A') # red dots
ax.plot(B_input_chars, B_time, 'bo-', label='Algo. B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left') # Show and place the legend fig.set_facecolor('white')
fig.savefig('graph_data')
