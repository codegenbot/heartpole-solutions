import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if severely low alertness or high health risks
    if alertness < 0.4 or hypertension > 0.06 or intoxication > 0.07 or time_since_slept >= 8.0:
        return 3

    # Take coffee to increase alertness if it's low but hypertension is manageable
    if alertness < 0.5 and hypertension <= 0.03:
        return 1

    # Drink beer only if it helps manage intoxication, assuming moderate thresholds
    if 0.5 <= alertness < 0.65 and intoxication <= 0.03 and hypertension <= 0.02:
        return 2

    # Default action is to just work if conditions are non-critical
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)