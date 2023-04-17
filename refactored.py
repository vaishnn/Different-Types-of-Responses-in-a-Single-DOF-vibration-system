import questionary
import sys
from calculations import calculate, plot_graph

def get_float_input(prompt):
    # function to get input and convert it to float
    while True:
        try:
            user_input = questionary.text(prompt).ask()
            float_input = float(user_input)
            return float_input
        except ValueError:
            print("Please enter valid float number.")
        except:
            sys.exit(1)

def motd():
    # message to print when program starts
    logo = """
=================================================================

 ▄▄   ▄▄ ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ 
█  █ █  █   █  ▄    █   ▄  █ █      █       █   █       █  █  █ █
█  █▄█  █   █ █▄█   █  █ █ █ █  ▄   █▄     ▄█   █   ▄   █   █▄█ █
█       █   █       █   █▄▄█▄█ █▄█  █ █   █ █   █  █ █  █       █
█       █   █  ▄   ██    ▄▄  █      █ █   █ █   █  █▄█  █  ▄    █
 █     ██   █ █▄█   █   █  █ █  ▄   █ █   █ █   █       █ █ █   █
  █▄▄▄█ █▄▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█▄█ █▄▄█ █▄▄▄█ █▄▄▄█▄▄▄▄▄▄▄█▄█  █▄▄█
 ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄ ▄▄▄     ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █  █  █ █      █   █   █  █ █  █       █       █   ▄  █  
█   ▄   █   █▄█ █  ▄   █   █   █  █▄█  █▄▄▄▄   █    ▄▄▄█  █ █ █  
█  █▄█  █       █ █▄█  █   █   █       █▄▄▄▄█  █   █▄▄▄█   █▄▄█▄ 
█       █  ▄    █      █   █▄▄▄█▄     ▄█ ▄▄▄▄▄▄█    ▄▄▄█    ▄▄  █
█   ▄   █ █ █   █  ▄   █       █ █   █ █ █▄▄▄▄▄█   █▄▄▄█   █  █ █
█▄▄█ █▄▄█▄█  █▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█

=================================================================
    """
    print(logo)
    print("[!!] Enter all values in SI Units only.")

def external_force():
    # function to get details about forced vibrations
    choices = ["1. Free vibration", "2. Harmonically Forced Vibration"]
    forced_flag = None
    harmonic_force = {
    "amplitude": 0.0,
    "frequency": 0.0,
    }
    while forced_flag == None:
        user_choice = questionary.select("Choose type of vibration", choices).ask()
        if user_choice[0] == '1':
            forced_flag = 0 
        elif user_choice[0] == '2':
            forced_flag = 1
            harmonic_force["amplitude"] = get_float_input("Enter the amplitude of harmonic force:")
            harmonic_force["frequency"] = get_float_input("Enter the frequency of harmonic force:")
    return forced_flag, harmonic_force

if __name__ == "__main__":
    motd()

    mass = get_float_input("Enter the mass of the body (m) :")
    stiffness = get_float_input("Enter the stiffnes of the spring (k) :")
    damping_coeff = get_float_input("Enter damping coefficient (C) [Enter 0 if undamped]:")
    forced_flag, harmonic_force = external_force()
    init_time = get_float_input("Enter initial time at which the simulation is started:")
    time = get_float_input("Enter amount of time for which to run the simulation:")
    init_position = get_float_input("Enter initial position of vibrating mass:")
    init_velocity = get_float_input("Enter initial velocity of vibrating mass:")

    # doing the calculations:
    calculate(mass, stiffness, from_time=init_time, to_time=(init_time+time), init_pos=init_position, init_vel=init_velocity, damping_coefficient=damping_coeff, amount_of_force=harmonic_force["amplitude"], frequency_of_force=harmonic_force["frequency"])
