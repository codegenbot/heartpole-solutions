import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Use beer strategically to balance high alertness with social factors:
    if alertness > 0.85 and hypertension < 0.03 and intoxication < 0.03:
        return 2

    # Prioritize rest in more pivotal thresholds:
    if hypertension > 0.06 or intoxication > 0.1:
        return 3
    if time_since_slept > 4:
        return 3
    if alertness < 0.55:
        return 3

    # Coffee can be a more accessible booster:
    if alertness < 0.7 and hypertension < 0.04 and intoxication < 0.04:
        return 1

    # Increase work viability:
    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.04:
        return 0

    # Default to sleep if conditions aren't met:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)