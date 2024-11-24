import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when severely lacking sleep, hypertension, or intoxication is high
    if alertness <= 0.2 or hypertension >= 0.8 or intoxication >= 0.7 or time_since_slept >= 8:
        return 3  # Sleep to recover

    # Optimal working condition
    if alertness > 0.7 and hypertension < 0.5 and intoxication < 0.5:
        return 0  # Just work

    # Use coffee to boost alertness when moderately low and health allows
    if 0.3 <= alertness <= 0.6 and hypertension < 0.6 and intoxication < 0.5:
        return 1  # Drink coffee and work

    # Consider using beer if alertness is adequate and intoxication is low, to correct high hypertension
    if 0.5 <= alertness and hypertension > 0.5 and intoxication < 0.4:
        return 2  # Drink beer and work

    # Fall back to sleep to default recovery mode
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)