import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: adjust intoxication and hypertension thresholds
    if intoxication > 0.15 or hypertension > 0.02 or time_since_slept >= 8:
        return 3  # sleep
    
    # Consider moderate conditions and balance
    if hypertension > 0.015 or intoxication > 0.1:
        return 2  # drink beer and work

    # Adjust productivity optimization
    if alertness < 0.6:
        return 1  # drink coffee and work
    if time_elapsed > 500 and work_done < 300:
        return 1  # boost productivity if behind
    
    return 0  # just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)