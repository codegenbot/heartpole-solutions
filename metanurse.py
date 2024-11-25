import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep frequently to maintain alertness and health
    if (
        hypertension > 0.1
        or intoxication > 0.03
        or alertness < 0.7
        or time_since_slept >= 3
    ):
        return 3
    # Use coffee only when safe and beneficial
    if alertness < 0.85 and hypertension < 0.07 and intoxication <= 0.01:
        return 1
    # Work only under safe health conditions
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)