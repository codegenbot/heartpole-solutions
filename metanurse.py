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

    # Prioritize sleep for critical health conditions
    if (
        hypertension > 0.12
        or intoxication > 0.002
        or time_since_slept > 3.0
        or alertness < 0.10
    ):
        return 3  # sleep

    # Drink coffee if alertness is low and health conditions are good
    if alertness < 0.20 and intoxication < 0.001 and hypertension < 0.03:
        return 1  # drink coffee and work

    # Drink beer if work done is low and health conditions are good
    if work_done < 0.10 and intoxication < 0.001 and hypertension < 0.03:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)