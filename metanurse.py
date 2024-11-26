import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if health is severely compromised
    if hypertension > 0.015 or intoxication > 0.05:
        return 3

    # Prioritize sleep for sleep deprivation or very low alertness
    if time_since_slept > 5 or alertness < 0.4:
        return 3

    # Consume coffee to boost moderate alertness if health is safe
    if 0.4 <= alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1

    # Drink beer periodically for alert balance with minimal health risk
    if (
        time_elapsed >= 200
        and time_elapsed % 150 == 0
        and hypertension < 0.008
        and intoxication < 0.015
    ):
        return 2

    # Default to regular work if conditions allow
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)