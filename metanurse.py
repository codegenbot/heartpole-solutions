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

    if hypertension > 0.003 or intoxication > 0.0003 or time_since_slept > 0.003:
        return 3  # sleep

    if alertness < 0.7 and intoxication < 0.0003 and hypertension < 0.003:
        return 1  # drink coffee and work

    if work_done < 0.003 and intoxication < 0.0003 and hypertension < 0.003:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)