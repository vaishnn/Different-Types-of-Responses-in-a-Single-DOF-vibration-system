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