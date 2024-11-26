import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for high-risk hypertension or intoxication
    if hypertension > 0.03 or intoxication > 0.08:
        return 3

    # Use beer to manage moderate hypertension
    if 0.02 < hypertension <= 0.03 and intoxication < 0.06 and alertness > 0.5:
        return 2

    # Sleep if alertness is very low or sleep deprivation is high
    if time_since_slept > 6 or alertness < 0.35:
        return 3

    # Coffee boost if alertness is low but health is stable
    if alertness < 0.5 and hypertension < 0.02 and intoxication < 0.04:
        return 1

    # Default work if health indicators remain stable
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)