import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for critical conditions
    if alertness < 0.5 or hypertension >= 0.05 or intoxication >= 0.06:
        return 3

    # If time_since_slept is high but alertness is still reasonable, prioritize sleep
    if time_since_slept > 6 or (time_since_slept > 4 and alertness < 0.7):
        return 3
    
    # Use coffee if alertness is moderate and health allows it
    if 0.6 <= alertness < 0.8 and hypertension < 0.02 and time_since_slept <= 3:
        return 1

    # Work when alertness is high and health indicators are stable
    if alertness >= 0.8 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    # Drink beer only if health is perfect and needing a low-key boost
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 2
    
    # Default to work as a fallback if conditions are moderate
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)