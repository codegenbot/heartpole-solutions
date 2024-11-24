import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health indicators are above baseline or haven't slept recently
    if alertness < 0.5 or hypertension >= 0.5 or intoxication >= 0.3 or time_since_slept >= 6:
        return 3  # Must sleep

    # Work if all health indicators are stable and effective
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee if alertness is dropping but manage hypertension and intoxication
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Resort to careful beer use under relaxed health conditions
    if alertness < 0.6 and intoxication < 0.2 and hypertension < 0.4:
        return 2  # Drink beer and work

    # Fallback to sleep if no better options
    return 3  # Sleep if no other option is optimal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)