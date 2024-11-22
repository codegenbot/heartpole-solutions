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

    if time_since_slept > 16 or alertness < 0.2:
        return 3  # sleep
    elif alertness < 0.5 and intoxication < 0.2 and hypertension < 0.6:
        return 1  # drink coffee and work
    elif hypertension < 0.4 and intoxication < 0.4:
        return 2  # drink beer and work
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)