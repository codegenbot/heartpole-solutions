import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health risks
    if (
        alertness < 0.5
        or hypertension > 0.4
        or intoxication > 0.2
        or time_since_slept > 6
    ):
        return 3

    # Use coffee carefully to maintain alertness without increasing risk
    if alertness < 0.7 and hypertension <= 0.3 and intoxication <= 0.1:
        return 1

    # Prioritize work with stable conditions
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication <= 0.05:
        return 0

    # Beer as a very last resort, almost never
    if intoxication < 0.03 and hypertension < 0.2:
        return 2

    # Default to sleep if conditions are ambiguous
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)