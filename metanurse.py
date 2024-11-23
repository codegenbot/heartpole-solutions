import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are concerning
    if hypertension > 0.25 or intoxication > 0.2:
        return 3  # Sleep

    # Encourage sleep when alertness is low
    if alertness < 0.8:
        return 3  # Sleep

    # Strategic coffee use if alertness is medium and health factors are low
    if 0.8 <= alertness < 0.9 and hypertension < 0.15 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Earlier sleep if significant time has passed since last sleeping
    if time_since_slept > 3:
        return 3  # Sleep

    # Default to work when all metrics are within optimal ranges
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)