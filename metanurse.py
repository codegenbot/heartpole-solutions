import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if any health indicator is critically off or sleep is overdue
    if alertness < 0.5 or hypertension >= 0.35 or intoxication >= 0.15 or time_since_slept >= 4:
        return 3  # Must sleep immediately
    
    # Use coffee only with moderate alertness and safe health indicators
    if alertness < 0.6 and hypertension < 0.25 and intoxication < 0.1 and time_since_slept < 3:
        return 1  # Drink coffee and work
    
    # Default action: just work if alertness is sufficient and health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)