import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is too low or health risks are too high
    if alertness < 0.4 or hypertension >= 0.7 or intoxication >= 0.7 or time_since_slept > 12:
        return 3  # Sleep to recover
    
    # Drink coffee if alertness is moderate to regain energy, considering health
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Just work if alertness is sufficient and health indicators are low
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.4:
        return 0  # Just work

    # Avoid any additional risk when health conditions are not ideal
    return 3  # Sleep to avoid health issues

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)