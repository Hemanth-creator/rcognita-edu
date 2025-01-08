import numpy as np
import matplotlib.pyplot as plt
circle_radius = 2
circle_Center = [0,0]
num_of_wp = 5
f =0.5
theta = np.linspace(0,2* np.pi, num_of_wp)
x_ref = np.linspace(0,5,200)
y_ref  = circle_radius * np.sin( 2*np.pi * x_ref *f)
theta1 = np.arctan(np.gradient(y_ref),np.gradient(x_ref)) 
plt.plot(x_ref,y_ref)
plt.show()





        