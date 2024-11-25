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
        hypertension > 0.7
        or intoxication > 0.03
        or time_since_slept > 10
        or alertness < 0.1
    ):
        return 3  # sleep

    if alertness < 0.3 and intoxication < 0.01 and hypertension < 0.5:
        return 1  # drink coffee and work

    return 0  # just work, avoid beer if health is at risk


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)