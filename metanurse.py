import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High priority to sleep if health conditions are bad or alertness too low
    if alertness < 0.4 or hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep
    
    # Sleep if overdue even if conditions don't seem critical
    if time_since_slept > 6:
        return 3  # Sleep

    # Moderate alertness: drink coffee, but check health
    if alertness < 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Safe to work
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)