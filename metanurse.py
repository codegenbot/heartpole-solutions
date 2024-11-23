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
        or alertness < 0.05
        or hypertension > 0.4
        or intoxication > 0.1
    ):
        return 3  # sleep to recover
    elif alertness < 0.1 and intoxication < 0.02 and hypertension < 0.05:
        return 1  # drink coffee and work
    elif (
        hypertension < 0.02
        and intoxication < 0.005
        and work_done < 0.05
        and alertness > 0.8
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