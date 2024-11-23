import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for critical health or alertness issues
    if hypertension > 0.3 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.4:
        return 3  # Sleep

    # Use coffee to boost productivity when alertness is moderately low and safe
    if alertness < 0.65 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Opt for beer only when intoxication is moderate but avoid frequent consumption
    if alertness < 0.6 and 0.1 < intoxication <= 0.15:
        return 2  # Drink beer and work

    # Default to working if conditions are stable for sustained productivity
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)