import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os
def calculate(mass, stiffness, from_time, to_time, init_pos, init_vel, damping_coefficient, amount_of_force, frequency_of_force):
    
    # Creating an numpy array
    time = np.arange(from_time,to_time,0.01);
    omega_natural = np.sqrt(stiffness/mass);
    pos_arr_force = 0
    if amount_of_force == 0:
        if damping_coefficient == 0:
            # Undamped, free vibration
            position_arr = init_pos*np.cos(omega_natural*time) + init_vel/omega_natural*np.sin(omega_natural*time);
        else:
            # Damped, free vibration
            zeta = damping_coefficient/(2*mass*omega_natural);
            if zeta < 1:
                # Underdamped, free vibration
                position_arr = np.exp(-zeta*omega_natural*time)*(init_pos*np.cos(np.sqrt(1-zeta**2)*omega_natural*time) + ((init_vel + zeta*omega_natural)/
                                (np.sqrt(1-zeta**2)*omega_natural))*np.sin(np.sqrt(1-zeta**2)*omega_natural*time))
            elif zeta == 1:
                # Critically damped
                position_arr = np.exp(-omega_natural*time)*(init_pos + (init_vel + omega_natural*init_pos)*time)
            else:
                # Overdamped
                C1 = (init_pos * omega_natural * (zeta + np.sqrt(zeta**2 - 1)) + init_vel)/(2*omega_natural*np.sqrt(zeta**2 - 1))
                C2 = (-init_pos * omega_natural *(zeta - np.sqrt(zeta**2 - 1)) - init_vel)/(2*omega_natural*np.sqrt(zeta**2 - 1))
                position_arr = C1*np.exp((-zeta + np.sqrt(zeta**2 - 1))*omega_natural*time) + C2*np.exp((-zeta - np.sqrt(zeta**2 - 1))*omega_natural*time)
    else:
        if damping_coefficient == 0:
            # Undamped under Harmonic Force
            position_arr = ((init_pos - amount_of_force/(stiffness - mass * frequency_of_force**2))*np.cos(omega_natural*time) + (init_vel/omega_natural)*np.sin(omega_natural*time) + 
                            (amount_of_force/(stiffness - mass * frequency_of_force**2)*np.cos(frequency_of_force*time)))
            pos_arr_force = (amount_of_force/(stiffness - mass * frequency_of_force**2)*np.cos(frequency_of_force*time))
        else:
            zeta = damping_coefficient/(2*mass*omega_natural)
            # Damped under Harmonic Force
            position_arr = (amount_of_force/stiffness)/np.sqrt((1-(frequency_of_force/omega_natural)**2)**2 + (2*zeta*frequency_of_force/omega_natural)**2)*np.sin(frequency_of_force*time-
                            np.arctan(2*zeta*frequency_of_force/omega_natural/(1-(frequency_of_force/omega_natural)**2)))
    plot_graph(position_arr,time)




def plot_graph(position_matrix,time_matrix):
    plt.figure(figsize=(30,15))
    plt.plot(time_matrix,position_matrix,label = 'response');
    plt.grid(True)
    plt.legend()
    plt.savefig("Vibration Plot")
    im = Image.open("Vibration Plot.png")
    im.show()