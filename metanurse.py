import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if any condition is risky
    if (
        alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.25
        or time_since_slept > 7
    ):
        return 3  # Sleep to prevent health issues

    # Drink coffee to boost alertness when it's low but health conditions are stable
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.1 and time_since_slept <= 7:
        return 1  # Drink coffee and work

    # Work with default action if conditions are optimal
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication < 0.2:
        return 0  # Continue working
    
    # Consider beer for mild intoxication with safe hypertension levels    
    if intoxication >= 0.15 and hypertension < 0.6:
        return 2  # Drink beer and work

    return 0  # Default to working under stable conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)