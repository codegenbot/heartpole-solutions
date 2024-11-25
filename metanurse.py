import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.3 or hypertension > 0.1 or time_since_slept >= 2.5:
        return 3  # Prioritize sleep if critical conditions are met.

    if alertness < 0.5 and intoxication <= 0.02:
        return 1  # Use coffee to boost productivity.

    if alertness >= 0.8 and hypertension < 0.03 and intoxication < 0.01:
        return 0  # Work efficiently if fully alert and health is good.

    if 0.5 <= alertness < 0.8 and hypertension < 0.05:
        return 1  # Use coffee to maintain productivity.

    if work_done < 0.02 and alertness < 0.35 and intoxication < 0.05:
        return 2  # Consider beer to relax and improve low productivity.

    return 0  # Default to just working if conditions are reasonably good.


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)