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

    if alertness < 0.1 or time_since_slept > 0.03:
        return 3  # Sleep if alertness is very low or time since slept is high

    if alertness < 0.2 and intoxication < 0.000001 and hypertension < 0.001:
        return 1  # Drink coffee and work if alertness is low and conditions are safe

    if work_done < 0.7 and intoxication < 0.000001 and hypertension < 0.001:
        return 2  # Drink beer and work if work done is low and conditions are safe

    return 0  # Just work otherwise


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)