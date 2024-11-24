import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are critical
    if hypertension > 0.75 or intoxication > 0.5 or time_since_slept >= 5:
        return 3
    if alertness < 0.3:
        return 3
    # Allow coffee to boost alertness if it is moderately low and health indicators support it
    if alertness < 0.5 and hypertension <= 0.6 and intoxication <= 0.25:
        return 1
    # Prefer just work if alertness is sufficiently high
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0
    # Beer and work only if health is not too compromised
    if hypertension <= 0.6 and intoxication < 0.3:
        return 2
    # Default to sleep in uncertain situations
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)