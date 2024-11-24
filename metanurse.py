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

    # Aggressively prioritize health
    if (
        hypertension > 0.5
        or intoxication > 0.1
        or time_since_slept > 15
        or alertness < 0.05
    ):
        return 3  # sleep

    # If alertness is low and not intoxicated or hypertensive, drink coffee
    if alertness < 0.15 and intoxication < 0.02 and hypertension < 0.15:
        return 1  # drink coffee and work

    # If work done is low and not intoxicated or hypertensive, drink beer
    if work_done < 0.1 and intoxication < 0.02 and hypertension < 0.15:
        return 2  # drink beer and work

    # If work is already done, sleep
    if work_done > 0.7:
        return 3  # sleep

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)