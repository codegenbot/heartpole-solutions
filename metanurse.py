import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if any health indicator is too low/critical
    if alertness < 0.5 or hypertension >= 0.3 or intoxication >= 0.15 or time_since_slept >= 5:
        return 3  # Must sleep immediately
    
    # Use coffee to boost alertness but ensure health is not compromised
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.1 and time_since_slept < 4:
        return 1  # Drink coffee and work
    
    # Consider beer only if alertness needs slight improvement and health is stable
    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.05:
        return 2  # Drink beer and work
    
    # Just work if health indicators are satisfactory and alertness is sufficient
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)