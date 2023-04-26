# Vibration Analyzer
## Group Members
- 2020UME1838 - Rohit Kaushal
- 2020UME1839 - Divyansh Rawat
- 2020UME1840 - Vaishnav Pratap
- 2020UME1841 - Kunal Sharma
- 2020UME1843 - Harsh Maniyar

## main.py
```python
from vib_type import *
from forced_or_not import *
from mass_stiffness import *
from init_cond import *
from time_for_run import *
from calculations import *

#Taking mass and stiffness from the user
print("Enter Every Value in SI units")
mass,stiffness = mass_stiffness_in();

# Asking user about if vibration is damped or not and then asking for damping coefficient
type_of_vibrr = type_of_vib();
if type_of_vibrr == 1:
    damping_coefficient = damping_coeff();
else:
    damping_coefficient = 0

# Asking user if vibration is forced or not
forrce = forced()
if forrce == 1:
    amount_of_force = amt_force()
    frequency_of_force = freq_in()
else:
    amount_of_force = 0
    frequency_of_force = 0;

# Asking user to enter Intital Conditions
print("Enter Conditions at t=0\n")
init_pos, init_vel = initial_conditions();

# Asking user to enter time constraints
print("Enter the time which needs to be plotted")
from_time, total_time = time_to_run()
to_time = total_time + from_time;

# Calling the Calculating function to calculate and plot the graph
calculate(mass, stiffness, from_time, to_time, init_pos, init_vel, damping_coefficient = damping_coefficient, amount_of_force = amount_of_force, frequency_of_force = frequency_of_force)

```

## calculations.py
```python
import numpy as np
from matplotlib import pyplot as plt
# from PIL import Image
import os
def calculate(mass, stiffness, from_time, to_time, init_pos, init_vel, damping_coefficient, amount_of_force, frequency_of_force):
    note= """
    Important to Note:
        - the variables `init_pos` and `init_vel`  represent the conditions at t=0 and not at `from_time`
        - the variables `from_time` and `to_time` only represent the time to be plotted on graph
    """
    print(note)
    
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
                position_arr = np.exp(-zeta*omega_natural*time)*(init_pos*np.cos(np.sqrt(1-zeta**2) * omega_natural*time) + ((init_vel + zeta*omega_natural)/
                                (np.sqrt(1-zeta**2) * omega_natural)) * np.sin(np.sqrt(1-zeta**2) * omega_natural*time))
            elif zeta == 1:
                # Critically damped
                position_arr = np.exp(-omega_natural*time)*(init_pos + (init_vel + omega_natural*init_pos) * time)
            else:
                # Overdamped
                C1 = (init_pos * omega_natural * (zeta + np.sqrt(zeta**2 - 1)) + init_vel)/(2*omega_natural*np.sqrt(zeta**2 - 1))
                C2 = (-init_pos * omega_natural *(zeta - np.sqrt(zeta**2 - 1)) - init_vel)/(2*omega_natural*np.sqrt(zeta**2 - 1))
                position_arr = C1*np.exp((-zeta + np.sqrt(zeta**2 - 1)) * omega_natural*time) + C2*np.exp((-zeta - np.sqrt(zeta**2 - 1)) * omega_natural*time)
    else:
        if stiffness - mass * frequency_of_force**2 == 0:
            print("Condition of Resonance");
            return
        if damping_coefficient == 0:
            # Undamped under Harmonic Force
            position_arr = ((init_pos - amount_of_force/(stiffness - mass * frequency_of_force**2)) * np.cos(omega_natural*time) + (init_vel/omega_natural) * np.sin(omega_natural*time) + 
                            (amount_of_force/(stiffness - mass * frequency_of_force**2) * np.cos(frequency_of_force*time)))
            pos_arr_force = (amount_of_force/(stiffness - mass * frequency_of_force**2) * np.cos(frequency_of_force*time))
        else:
            zeta = damping_coefficient/(2*mass*omega_natural)
            if zeta < 1:
                # Underdamped, free vibration
                position_arr1 = np.exp(-zeta*omega_natural*time)*(init_pos*np.cos(np.sqrt(1-zeta**2) * omega_natural*time) + ((init_vel + zeta*omega_natural)/
                                (np.sqrt(1-zeta**2) * omega_natural)) * np.sin(np.sqrt(1-zeta**2) * omega_natural*time))
            elif zeta == 1:
                # Critically damped
                position_arr1 = np.exp(-omega_natural*time)*(init_pos + (init_vel + omega_natural*init_pos) * time)
            else:
                # Overdamped
                C1 = (init_pos * omega_natural * (zeta + np.sqrt(zeta**2 - 1)) + init_vel)/(2*omega_natural*np.sqrt(zeta**2 - 1))
                C2 = (-init_pos * omega_natural *(zeta - np.sqrt(zeta**2 - 1)) - init_vel)/(2*omega_natural*np.sqrt(zeta**2 - 1))
                position_arr1 = C1*np.exp((-zeta + np.sqrt(zeta**2 - 1)) * omega_natural*time) + C2*np.exp((-zeta - np.sqrt(zeta**2 - 1)) * omega_natural*time)
            # Damped under Harmonic Force
            position_arr = (amount_of_force/stiffness)/np.sqrt((1-(frequency_of_force/omega_natural)**2)**2 + (2*zeta*frequency_of_force/omega_natural)**2) * np.sin(frequency_of_force*time- 
                            np.arctan(2*zeta*frequency_of_force / omega_natural/(1-(frequency_of_force/omega_natural)**2))) + position_arr1
    plot_graph(position_arr,time)




def plot_graph(position_matrix,time_matrix):
    plt.figure(figsize=(30,15))
    plt.plot(time_matrix,position_matrix,label = 'response');
    plt.grid(True)
    plt.legend()
    plt.savefig("Vibration Plot")
    plt.show()
    # im = Image.open("Vibration Plot.png")
    # im.show()

```

## forced_or_not.py
```python
def forced(n_val = 1):
    if n_val == 1:
        # Taking input as a string
        print("Enter the type of Vibration \n\nIs it forced harmonically or not forced \n\nEnter 1 for forced harmonically and 0 for not forced")
    force = input();
    # A value for the loop which will decide when to exit the loop
    gar_val = 0
    while not(gar_val):
        # Using try and except for Wrong input
        try:
            force = int(force);
            gar_val = 1
        except Exception:
            print("Wrong input type, Enter a integer value")
            gar_val = 0
            force = input();
    if force == 1:
        print("HARMONICALLY FORCED")
    elif force == 0:
        print("NOT FORCED")
    else:
        print("Wrong input, Input again")
        # Using Recursion in place of loop iteration
        return(forced(n_val=0));
    return force;




def amt_force(n_val1 = 1):
    if n_val1 == 1:
        # Taking input as a string
        print("Enter the amount of force")
    am_force = input();
    # A value for the loop which will decide when to exit the loop
    gar_val1 = 0
    while not(gar_val1):
        # Using try and except for Wrong input
        try:
            am_force = float(am_force);
            gar_val1 = 1
            if am_force == 0:
                raise Exception
        except Exception:
            print("Wrong input type, Enter a integer value")
            gar_val1 = 0
            am_force = input();
    return am_force;




def freq_in(n_val2 = 1):
    if n_val2 == 1:
        print("Enter the frequency of the harmonic force")
    freq = input();
    gar_val1 = 0;
    while not(gar_val1):
        # Using try and except for Wrong input
        try:
            freq = float(freq);
            gar_val1 = 1
        except Exception:
            print("Wrong input type, Enter a integer value")
            gar_val1 = 0
            freq = input();
    if freq < 0:
        print("Excitation frequency cannot be negative\nEnter the freq again")
        freq_in(n_val2=0)
    return freq;
```

## mass_stiffness.py
```python
def mass_stiffness_in():
    # Taking Mass from the user
    print("Mass of the body")
    while True:
        try:
            mass = float(input())
            if mass <= 0:
                raise Exception
        except Exception:
            print("Enter a acceptable value of mass")
        else:
            break
    # Taking Stiffness of spring from the user
    print("Stiffness of the spring")
    while True:

        try:
            stiff = float(input())
            if stiff <= 0:
                raise Exception
        except Exception:
            print("Enter a acceptable value of stiffness")
        else:
            break
    return mass, stiff
```

## time_for_run.py
```python
def time_to_run():
    print("Enter the time at which the simulation should be started:")
    while True:
        try:
            init_time = float(input())
        except Exception:
            print("Enter an acceptable value of time")
        else:
            break
    
    print("Enter the time for which you want to run the simulation")
    while True:
        try:
            time = float(input())
            if time < 0: 
                raise Exception
        except Exception:
            print("Enter an acceptable value of time frame")
        else:
            break
    return init_time,time;


```

## vib_type.py
```python
def type_of_vib(n_val = 1):
    if n_val == 1:
        # Taking input as a string
        print("Enter the type of Vibration (Damped or Undamped) \nEnter 1 for damped and 0 for undamped")
    vib = input();
    
    # A value for the loop which will decide when to exit the loop
    gar_val = 0
    while not(gar_val):

        # Using try and except for Wrong input
        try:
            vib = int(vib);
            if not(vib == 0 or vib == 1):
                raise Exception
            gar_val = 1
        except Exception:
            print("Wrong input type, Enter a acceptable value")
            gar_val = 0
            vib = input();
    if vib == 1:
        print("DAMPED")
    elif vib == 0:
        print("UNDAMPED")
    return vib;




def damping_coeff(n_val3 = 1):
    if n_val3 == 1:
        print("Enter damping coefficient")
    dam = input();
    gar_val3 = 0
    while not(gar_val3):

        # Using try and except for Wrong input
        try:
            dam = float(dam);
            if dam <= 0:
                raise Exception
            gar_val3 = 1
        except Exception:
            print("Wrong input, Enter a positive integer value")
            gar_val3 = 0
            dam = input();
    return dam;
```

## init_cond.py
```python
def initial_conditions():
    # print("Enter initial position")
    print("Enter position at t=0")
    while True:
        try:
            init_position = float(input());
        except Exception:
            print("Enter a acceptable initial position")
        else:
            break
    print("Enter velocity at t=0")
    while True:
        try:
            init_vel = float(input());
        except Exception:
            print("Enter a acceptable initial velocity")
        else:
            break
    return init_position, init_vel;

```

## Output for test cases
![Free Undamped](../output/free-undamped.png)

![Free Damped](../output/free-damped.png)

![Forced Damped](../output/forced-damped.png)

