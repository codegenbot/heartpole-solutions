import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for critical health or alertness levels
    if hypertension > 0.25 or intoxication > 0.12 or time_since_slept > 7 or alertness < 0.55:
        return 3  # Sleep

    # Use coffee to boost alertness if it's moderately low
    if 0.55 <= alertness < 0.7 and hypertension <= 0.18 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Avoid beer unless necessary and its effects won't worsen conditions
    if alertness < 0.6 and 0.08 < intoxication <= 0.12:
        return 2  # Drink beer and work

    # Default to working when conditions are stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)