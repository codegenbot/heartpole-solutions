import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if sleep-deprived or at risk due to health factors
    if time_since_slept > 5 or alertness < 0.4 or hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep
    
    # Coffee only if alertness is low but health is stable
    if alertness < 0.6 and hypertension <= 0.3 and intoxication < 0.2 and time_since_slept <= 4:
        return 1  # Drink coffee and work
    
    # Work if in healthy and alert state
    if alertness >= 0.7 and hypertension <= 0.25 and intoxication <= 0.1:
        return 0  # Just work
    
    # Beer if alertness needs boosting but under controlled conditions
    if alertness < 0.5 and hypertension < 0.35 and intoxication < 0.2:
        return 2  # Drink beer and work

    # If none of the specific conditions match, sleep as fallback
    return 3  # Fallback to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)