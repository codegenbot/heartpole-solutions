import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health by checking critical conditions for sleeping first
    if hypertension > 0.55 or intoxication > 0.3:
        return 3  # prioritizing sleep when health risk is detected
    if time_since_slept > 7:
        return 3  # need to sleep to maintain health
    
    # Balance productivity with moderate health status
    if alertness < 0.4:
        if time_elapsed < 5:
            return 1  # coffee to boost alertness
        else:
            return 3  # sleep if coffee isn't sufficient
    
    # If health measures are under control, focus on working
    if work_done < 0.5 and alertness > 0.5:
        return 0  # just work if alertness and productivity are good
    if time_since_slept > 5 and alertness < 0.7 and time_elapsed < 7:
        return 1  # drinking coffee to maintain productivity
    
    return 0  # default work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)