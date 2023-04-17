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