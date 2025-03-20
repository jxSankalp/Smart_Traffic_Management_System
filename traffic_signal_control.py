def control_traffic_signal(data):
    vehicle_count = data['vehicle_count']
    
    # Traffic light timing logic
    if vehicle_count < 10:
        signal_time = 20  # Green light for 20 seconds
    elif 10 <= vehicle_count < 30:
        signal_time = 40  # Green light for 40 seconds
    else:
        signal_time = 60  # Green light for 60 seconds

    print(f"Vehicle Count: {vehicle_count}, Green Signal Time: {signal_time} sec")


