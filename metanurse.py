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

    # Aggressively prioritize health conditions
    if hypertension > 0.15 or intoxication > 0.05 or time_since_slept > 6:
        return 3  # sleep

    # Ensure high alertness before considering other actions
    if alertness < 0.7 and intoxication < 0.01 and hypertension < 0.01:
        return 1  # drink coffee and work

    # Balance work and rest
    if work_done < 0.6 and intoxication < 0.01 and hypertension < 0.01:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)