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
        hypertension > 0.01
        or intoxication > 0.000001
        or time_since_slept > 0.2
        or alertness < 0.1
    ):
        return 3

    if alertness < 0.2 and intoxication < 0.000001 and hypertension < 0.003:
        return 1

    if work_done < 0.4 and intoxication < 0.000001 and hypertension < 0.003:
        return 2

    return 0


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)