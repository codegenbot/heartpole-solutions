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
        hypertension > 0.002
        or intoxication > 0.000002
        or time_since_slept > 0.05
        or alertness < 0.05
    ):
        return 3

    if alertness < 0.08 and intoxication < 0.000001 and hypertension < 0.001:
        return 1

    if work_done < 0.00002 and intoxication < 0.000001 and hypertension < 0.001:
        return 2

    return 0


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)