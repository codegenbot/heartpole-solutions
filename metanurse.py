import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if critical health conditions are met
    if (
        alertness < 0.5
        or hypertension > 0.7
        or intoxication > 0.45
        or time_since_slept > 10
        or time_elapsed > 800
    ):
        return 3  # Need sleep

    # Use coffee if alertness is moderately low and there are minimal health risks
    if 0.5 <= alertness < 0.8 and hypertension < 0.6 and intoxication < 0.1:
        return 1  # Coffee and work

    # Just work if alertness is high and health metrics are safe
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.05:
        return 0  # Just work

    # Use beer to maintain some alertness when slightly intoxicated
    if alertness < 0.5 and 0.05 < intoxication <= 0.3 and hypertension < 0.5:
        return 2  # Beer and work

    # Default to sleep to recover
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)