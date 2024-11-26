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
        hypertension > 0.25
        or intoxication > 0.00003
        or time_since_slept > 3.0
        or alertness < 0.1
    ):
        return 3  # sleep

    # Drink coffee if alertness is low and conditions are safe
    if alertness < 0.25 and intoxication < 0.00003 and hypertension < 0.25:
        return 1  # drink coffee and work

    # Only drink beer if work is not progressing and conditions are safe
    if work_done < 0.00003 and intoxication < 0.00003 and hypertension < 0.25:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)