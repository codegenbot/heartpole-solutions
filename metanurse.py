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
        time_since_slept > 3
        or alertness < 0.3
        or hypertension > 0.2
        or intoxication > 0.01
    ):
        return 3  # sleep to recover
    elif 0.3 < alertness < 0.5 and intoxication < 0.005 and hypertension < 0.1:
        return 1  # drink coffee and work
    elif (
        alertness > 0.5
        and intoxication < 0.005
        and hypertension < 0.15
        and work_done < 0.7
    ):
        return 0  # just work
    else:
        return 2  # drink beer and work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = decide_action(observations)
    print(action)