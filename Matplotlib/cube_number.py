import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
cubes= [1,8,27,64,125]

plt.style.use('dark_background')
fig,ax = plt.subplots()
ax.plot(x_values,cubes,linewidth=3)


#Set chart title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', labelsize=14)


plt.show()