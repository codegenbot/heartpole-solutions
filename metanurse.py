import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health status
    if hypertension > 0.06 or intoxication > 0.05:
        return 3

    # Sleep if alertness is too low or hasn't slept for a long time
    if alertness < 0.6 or time_since_slept > 3:
        return 3

    # Drink coffee if confidence in work and moderate alertness with minimal hypertension
    if 0.6 <= alertness < 0.75 and hypertension < 0.02:
        return 1

    # Drink beer only if there's a mild need and safe intoxication level
    if 0.7 <= alertness < 0.85 and intoxication < 0.01:
        return 2

    # Work if alertness is high enough (more strictly defined)
    if alertness >= 0.85:
        return 0

    # If unsure, prioritize health by sleeping
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)