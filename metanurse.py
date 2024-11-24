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
        or time_since_slept > 0.05
        or alertness < 0.01
    ):
        return 3  # sleep

    # If alertness is low and not intoxicated or hypertensive, drink coffee
    if alertness < 0.2 and intoxication < 0.000002 and hypertension < 0.0002:
        return 1  # drink coffee and work

    # If work done is low and not intoxicated or hypertensive, drink beer (but not if alertness is too low)
    if (
        work_done < 0.1
        and intoxication < 0.000002
        and hypertension < 0.0002
        and alertness > 0.1
    ):
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)