import sys


def decide_action(observations):
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = observations

    if (
        time_since_slept > 4
        or alertness < 0.05
        or hypertension > 0.3
        or intoxication > 0.02
    ):
        return 3  # sleep to recover
    elif 0.1 < alertness < 0.25 and intoxication < 0.01 and hypertension < 0.1:
        return 1  # drink coffee and work
    elif (
        alertness > 0.25
        and intoxication < 0.015
        and hypertension < 0.15
        and work_done < 0.4
    ):
        return 2  # drink beer and work
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = decide_action(observations)
    print(action)