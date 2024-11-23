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
        time_since_slept > 2.5
        or alertness < 0.05
        or hypertension > 0.2
        or intoxication > 0.1
    ):
        return 3  # sleep to recover
    elif alertness < 0.2 and intoxication < 0.01 and hypertension < 0.03:
        return 1  # drink coffee and work
    elif hypertension < 0.01 and intoxication < 0.005 and work_done < 0.03:
        return 2  # drink beer and work (use sparingly)
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = decide_action(observations)
    print(action)