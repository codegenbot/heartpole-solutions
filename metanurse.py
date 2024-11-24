import sys


def choose_action(observations):
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = observations

    # Prioritize health
    if (
        hypertension > 0.015
        or intoxication > 0.000002
        or time_since_slept > 0.25
        or alertness < 0.08
    ):
        return 3

    # If alertness is low and health is okay, drink coffee
    if alertness < 0.15 and intoxication < 0.000002 and hypertension < 0.01:
        return 1

    # If work is not done and health is okay, drink beer
    if work_done < 0.5 and intoxication < 0.000002 and hypertension < 0.01:
        return 2

    # Default action: just work
    return 0


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)