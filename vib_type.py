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