import sys


def choose_action(observations):
    alertness, hypertension, intoxication, time_since_slept, _, _ = observations

    if (
        hypertension > 0.5
        or intoxication > 0.01
        or time_since_slept > 2.0
        or alertness < 0.2
    ):
        return 3  # sleep
    elif alertness < 0.4 and intoxication < 0.005 and hypertension < 0.3:
        return 1  # drink coffee and work
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)