import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if any health indicator is critically off or sleep is overdue
    if alertness < 0.7 or hypertension >= 0.4 or intoxication >= 0.2 or time_since_slept >= 4.0:
        return 3  # Must sleep immediately
    
    # Use coffee more aggressively for better boosting while being cautious
    if alertness < 0.8 and hypertension < 0.35 and intoxication < 0.1 and time_since_slept < 3.0:
        return 1  # Drink coffee and work
    
    # Allow beer for a minor boost in constrained situations
    if alertness < 0.7 and hypertension < 0.2 and intoxication < 0.15:
        return 2  # Drink beer and work
    
    # Default action: just work if alertness is sufficient and health metrics are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)