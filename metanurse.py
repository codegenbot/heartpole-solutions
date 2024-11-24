import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if any health indicator is critically off or sleep is overdue
    if alertness < 0.6 or hypertension >= 0.4 or intoxication >= 0.2 or time_since_slept >= 4.5:
        return 3  # Must sleep immediately
    
    # Use coffee conservatively as a booster but check health first
    if alertness < 0.75 and hypertension < 0.35 and intoxication < 0.1 and time_since_slept < 3.5:
        return 1  # Drink coffee and work
    
    # Avoid beer unless minor boost required and health metrics low
    if alertness < 0.65 and hypertension < 0.2 and intoxication < 0.1:
        return 2  # Drink beer and work
    
    # Default action: just work if alertness is sufficient and health metrics are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)