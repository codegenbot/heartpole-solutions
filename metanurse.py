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
        hypertension > 0.03
        or intoxication > 0.0003
        or time_since_slept > 2
        or alertness < 0.1
    ):
        return 3  # sleep

    # Drink coffee if alertness is low and health conditions are okay
    if alertness < 0.2 and intoxication < 0.0003 and hypertension < 0.02:
        return 1  # drink coffee and work

    # Drink beer if work done is low and health conditions are okay
    if work_done < 0.2 and intoxication < 0.0003 and hypertension < 0.02:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)