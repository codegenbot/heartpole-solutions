import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Highest priority for sleeping for health and alertness recovery
    if hypertension > 0.25 or intoxication > 0.15 or alertness < 0.4 or time_since_slept >= 6:
        return 3
    
    # Utilize coffee to boost productivity when under safe limits
    if alertness < 0.5 and hypertension <= 0.15 and intoxication < 0.05 and time_since_slept < 6:
        return 1

    # Avoid beer usage; emphasize its conditional use only
    if alertness >= 0.6 and hypertension < 0.1 and intoxication < 0.05 and work_done < 0.3:
        return 2
    
    # Default action is to just work if conditions allow
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)