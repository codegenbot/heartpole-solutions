import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize Sleep for Health Recovery
    if (
        time_since_slept > 8
        or alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.6
    ):
        return 3  # Sleep

    # Use Coffee for Productivity with Safe Limits
    if 0.3 <= alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Avoid Beer if Health is Compromised and Consider Rest
    if intoxication < 0.3 and hypertension < 0.4 and alertness < 0.5:
        return 2  # Drink beer and work

    # Encourage Safe Productive Work
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    return 3  # Sleep if safety or conditions are uncertain


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)