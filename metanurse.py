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
        hypertension > 0.001
        or intoxication > 0.0000003
        or time_since_slept > 0.03
        or alertness < 0.3
    ):
        return 3

    if alertness < 0.5 and intoxication < 0.0000003 and hypertension < 0.0005:
        return 1

    if work_done < 0.9 and intoxication < 0.0000003 and hypertension < 0.0005:
        return 2

    return 0


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)