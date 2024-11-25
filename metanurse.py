import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 6 or alertness < 0.5 or hypertension > 0.7 or intoxication > 0.2:
        return 3  # Sleep if conditions are risky
    if alertness > 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work if very alert and healthy
    if 0.6 <= alertness <= 0.8 and hypertension < 0.4:
        return 1  # Coffee and work if reasonably alert, but not optimal energy
    return 3  # Default to sleep as a safer fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)