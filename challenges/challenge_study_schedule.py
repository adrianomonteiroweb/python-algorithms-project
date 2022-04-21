def study_schedule(permanence_period, target_time):
    try:
        counting = 0
        
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counting += 1

        return counting
    except TypeError:
        return None            
