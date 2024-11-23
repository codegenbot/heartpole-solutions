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
        time_since_slept > 8
        or alertness < 0.05
        or hypertension > 0.9
        or intoxication > 0.8
    ):
        return 3  # sleep to recover
    elif alertness < 0.3 and intoxication < 0.05 and hypertension < 0.8:
        return 1  # drink coffee and work
    elif (
        hypertension < 0.05
        and intoxication < 0.01
        and work_done < 0.2
        and time_elapsed < 400
    ):
        return 2  # drink beer and work (use sparingly)
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = decide_action(observations)
    print(action)