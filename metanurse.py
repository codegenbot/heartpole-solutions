import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health status
    if hypertension > 0.07 or intoxication > 0.07:
        return 3

    # Sleep if alertness is too low or hasn't slept for a long time
    if alertness < 0.5 or time_since_slept > 4:
        return 3

    # Drink coffee if confidence in work and moderate alertness with minimal hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.03:
        return 1

    # Drink beer only if there's a mild need but always keep working when stable
    if 0.6 <= alertness < 0.8 and intoxication < 0.02:
        return 2

    # Work if alertness is high enough
    if alertness >= 0.8:
        return 0

    # Default to sleep if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)