import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.7
        or intoxication > 0.15
        or time_since_slept >= 4
    ):
        return 3  # Prioritize sleep more decisively
    if alertness < 0.8 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1  # Use coffee for moderate alertness boost
    if alertness >= 0.85 and hypertension < 0.3 and intoxication < 0.05:
        return 0  # Safe to work when conditions are optimal
    return 0  # Default action now always safe to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)