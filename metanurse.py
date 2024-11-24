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
        hypertension > 0.3
        or intoxication > 0.02
        or time_since_slept > 6
        or alertness < 0.1
    ):
        return 3  # sleep

    # Improve alertness if low and health conditions are met
    if alertness < 0.2 and intoxication < 0.02 and hypertension < 0.15:
        return 1  # drink coffee and work

    # Boost productivity if work done is low and health conditions are met
    if work_done < 0.2 and intoxication < 0.02 and hypertension < 0.15:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)