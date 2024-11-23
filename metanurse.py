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
        or alertness < 0.2
        or hypertension > 0.7
        or intoxication > 0.6
    ):
        return 3  # sleep to recover
    elif alertness < 0.4 and intoxication < 0.05 and hypertension < 0.5:
        return 1  # drink coffee and work
    elif hypertension < 0.1 and intoxication < 0.02 and work_done < 0.3:
        return 2  # drink beer and work (use sparingly)
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = decide_action(observations)
    print(action)