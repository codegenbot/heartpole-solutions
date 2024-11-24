import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for serious health issues or when time_since_slept is high
    if time_since_slept > 8 or hypertension >= 0.8 or intoxication >= 0.7:
        return 3
    # Sleep if alertness is critically low or haven't slept much
    if alertness < 0.5 or time_since_slept > 6:
        return 3
    # Opt for coffee if alertness is moderate and other conditions are mild
    if alertness < 0.7 and hypertension < 0.6:
        return 1
    # Default to work if alertness is high and health metrics are well within safe levels
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0
    # Use beer to balance if intoxication is acceptable
    return 2 if intoxication < 0.5 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
