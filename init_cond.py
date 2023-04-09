def initial_conditions():
    print("Enter initial position")
    while True:
        try:
            init_position = float(input());
        except Exception:
            print("Enter a acceptable initial position")
        else:
            break
    print("Enter initial velocity")
    while True:
        try:
            init_vel = float(input());
        except Exception:
            print("Enter a acceptable initial velocity")
        else:
            break
    return init_position, init_vel;
