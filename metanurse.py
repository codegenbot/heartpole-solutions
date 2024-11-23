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
        hypertension > 0.35
        or intoxication > 0.005
        or time_since_slept > 1.5
        or alertness < 0.05
    ):
        return 3  # sleep
    elif alertness < 0.15 and intoxication < 0.005 and hypertension < 0.25:
        return 1  # drink coffee and work
    elif work_done < 0.2 and intoxication < 0.005 and hypertension < 0.25:
        return 2  # drink beer and work
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)