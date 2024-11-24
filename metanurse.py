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
        hypertension > 0.6
        or intoxication > 0.15
        or time_since_slept > 12
        or alertness < 0.05
    ):
        return 3  # sleep

    # Boost alertness if low and safe
    if alertness < 0.2 and intoxication < 0.03 and hypertension < 0.2:
        return 1  # drink coffee and work

    # Increase work done if low and safe
    if work_done < 0.2 and intoxication < 0.03 and hypertension < 0.2:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)