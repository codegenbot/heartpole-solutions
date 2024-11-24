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
        hypertension > 0.01
        or intoxication > 0.000002
        or time_since_slept > 0.2
        or alertness < 0.05
    ):
        return 3  # sleep

    # If alertness is moderately low and not intoxicated or hypertensive, drink coffee
    if alertness < 0.6 and intoxication < 0.000002 and hypertension < 0.001:
        return 1  # drink coffee and work

    # If work done is significantly low and not intoxicated or hypertensive, drink beer
    if work_done < 0.4 and intoxication < 0.000002 and hypertension < 0.001:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)