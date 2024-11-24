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
        hypertension > 0.4
        or intoxication > 0.08
        or time_since_slept > 8
        or alertness < 0.15
    ):
        return 3  # sleep

    # Improve alertness if low
    if alertness < 0.25 and intoxication < 0.03 and hypertension < 0.2:
        return 1  # drink coffee and work

    # Boost productivity if work done is low
    if work_done < 0.2 and intoxication < 0.03 and hypertension < 0.2:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)