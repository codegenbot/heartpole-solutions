import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health conditions demand immediate sleep
    if hypertension > 0.2 or intoxication > 0.12:
        return 3
    
    # Aim for sleep with lower alertness or long periods without sleep
    if alertness < 0.7 or time_since_slept > 5:
        return 3
    
    # Use coffee more frequently for moderate alertness when health conditions allow
    if alertness < 0.75 and hypertension < 0.18 and intoxication < 0.1:
        return 1
    
    # Increase consideration for breaks based on time_elapsed and work_done
    if time_elapsed % 150 == 0 and work_done > 50:
        return 3
    
    # Avoid beer unless absolutely necessary (here, not used at all)
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)