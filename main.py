import numpy as np
import math 
import matplotlib.pyplot as plt

print("This Target Movement Prediction System is designed for defense applications. It helps track and predict the path of flying threats like drones or missiles, enabling accurate interception and neutralization.")
Speed = float(input("Enter the speed of the target(drone,missels)m/s:")) 
lanch_angle = int(input(f"Enter the Launch Angle of the target:(degrees):"))

x0,y0 = 0,0 #initail position
vx = Speed * math.cos(math.radians(lanch_angle)) 
vy = Speed * math.sin(math.radians(lanch_angle))
g = 9.8
flight = (2 *vy)/g #total time spent by the target in air
time = np.arange(0,flight,0.1)

x_position = []
y_position = []
for t in time:
    xt = x0 + vx * t #horizontal 
    yt = y0 + vy * t - 1/2 * g * t**2 #vertical 
    x_position.append(xt)
    y_position.append(yt) 

t_max_height = vy / g
x_max_height = vx * t_max_height
y_max_height = y0 + vy * t_max_height - 0.5 * g * t_max_height**2   

print(f"Total Distance Traveled: {math.sqrt(x_position[-1]*2 + y_position[-1]*2):.2f} m")
print(f"Flight Time: {flight:.2f} seconds")
print(f"Maximum Height: {y_max_height:.2f} meters")

plt.title("Target prediction System")

plt.plot(x_position,y_position, color = "black", label = "Target Motion curve") #curve

plt.scatter([x0],[y0], color = "green", label = "Launch point")
plt.scatter(x_max_height,y_max_height, color = "orange", label = "Max height")
plt.scatter(x_position[-1],0, color = "red", label = "Impact point")
plt.legend()

plt.xlabel("Horizontal Distance")
plt.ylabel("Height Travelled")
plt.grid(True)
plt.axis("equal")
plt.show()
