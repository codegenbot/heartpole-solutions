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

    if alertness < 0.2 or time_since_slept > 0.05:
        return 3  # Sleep

    if alertness < 0.3 and intoxication < 0.000001 and hypertension < 0.002:
        return 1  # Drink coffee and work

    if work_done < 0.8 and intoxication < 0.000001 and hypertension < 0.002:
        return 2  # Drink beer and work

    return 0  # Just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)