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

    if (
        hypertension > 0.05
        or intoxication > 0.0005
        or time_since_slept > 3
        or alertness < 0.1
    ):
        return 3  # sleep

    if alertness < 0.2 and intoxication < 0.0005 and hypertension < 0.03:
        return 1  # drink coffee and work

    if work_done < 0.3 and intoxication < 0.0005 and hypertension < 0.03:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)