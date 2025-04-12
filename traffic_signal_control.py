def control_traffic_signal(vehicle_count, accident_status):
    """
    Control traffic signals based on vehicle count and accident status.

    Arguments:
    vehicle_count -- Count of vehicles detected.
    accident_status -- List with status for left, right, and straight lanes.

    Returns:
    dict: Contains traffic light status and green light duration.
    """
    traffic_status = {"left": "green", "right": "green", "straight": "green"}

    # Set green light duration based on vehicle count
    if vehicle_count > 20:
        green_duration = 60
    elif vehicle_count > 10:
        green_duration = 45
    else:
        green_duration = 30

    # Override traffic light for accident lanes
    for i, status in enumerate(accident_status):
        if status == "Accident":
            direction = ["left", "right", "straight"][i]
            traffic_status[direction] = "red"

    # Add green light duration to the response
    traffic_status["duration"] = green_duration

    return traffic_status
