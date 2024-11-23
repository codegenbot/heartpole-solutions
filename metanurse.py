import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on health and alertness criteria
    if hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness drops too low or if it's been too long since last sleep
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # Sleep

    # Use coffee when moderate alertness boost is needed and health allows
    if 0.5 <= alertness < 0.7 and hypertension <= 0.18 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Work normally if all conditions are stable
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.05:
        return 0  # Just work

    # Resort to beer as a last attempt to balance intoxication and work if necessary
    if alertness < 0.65 and 0.05 < intoxication <= 0.15:
        return 2  # Drink beer and work

    # Default to working if no other condition is strongly violated
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)