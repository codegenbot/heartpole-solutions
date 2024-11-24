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

    # Prioritize health more aggressively
    if (
        hypertension > 0.001
        or intoxication > 0.0000002
        or time_since_slept > 0.02
        or alertness < 0.002
    ):
        return 3  # sleep

    # If alertness is low and not intoxicated or hypertensive, drink coffee
    if alertness < 0.03 and intoxication < 0.0000002 and hypertension < 0.00002:
        return 1  # drink coffee and work

    # If work done is very low and not intoxicated or hypertensive, drink beer
    if work_done < 0.02 and intoxication < 0.0000002 and hypertension < 0.00002:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)