def time_to_run():
    print("Enter the Intial time for starting the simulation")
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

