import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Use sleep if exhaustion or excessive working spans
    if time_since_slept >= 5.0 or alertness < 0.2:
        return 3

    # Sleep for health risks
    if hypertension > 0.06 or intoxication > 0.05:
        return 3

    # Coffee for moderate alertness and stable health
    if 0.35 <= alertness < 0.65 and hypertension < 0.03 and intoxication < 0.02:
        return 1

    # Work if high alertness and very good health
    if alertness >= 0.75 and hypertension < 0.015 and intoxication < 0.01:
        return 0

    # Check work_done and time_elapsed for efficiency
    if work_done < 0.5 and time_elapsed < 8.0:
        return 0

    # Default to sleep if undecided
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)