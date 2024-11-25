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

    # Prioritize health
    if (
        hypertension > 0.001
        or intoxication > 0.000001
        or time_since_slept > 0.1
        or alertness < 0.02
    ):
        return 3  # sleep

    # Drink coffee only if alertness is very low and health is good
    if alertness < 0.05 and intoxication < 0.0000003 and hypertension < 0.0005:
        return 1  # drink coffee and work

    # Drink beer only if work is significantly behind and health is good
    if work_done < 0.0005 and intoxication < 0.0000003 and hypertension < 0.0005:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)