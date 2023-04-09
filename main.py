from vib_type import *
from forced_or_not import *
from mass_stiffness import *
from init_cond import *
from time_for_run import *
from calculations import *

#Taking mass and stiffness from the user
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
print("Enter intitial Conditions\n")
init_pos, init_vel = initial_conditions();

# Asking user to enter time constraints
from_time, total_time = time_to_run()
to_time = total_time + from_time;

# Calling the Calculating function to calculate and plot the graph
calculate(mass, stiffness, from_time, to_time, init_pos, init_vel, damping_coefficient = damping_coefficient, amount_of_force = amount_of_force, frequency_of_force = frequency_of_force)