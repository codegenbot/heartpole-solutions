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

    # Prioritize health conditions
    if (
        hypertension > 0.001
        or intoxication > 0.0000001
        or time_since_slept > 0.3
        or alertness < 0.2
    ):
        return 3  # sleep

    # Ensure alertness and avoid over-intoxication
    if alertness < 0.7 and intoxication < 0.0000001 and hypertension < 0.001:
        return 1  # drink coffee and work

    # Balance work and rest
    if work_done < 0.0000001 and intoxication < 0.0000001 and hypertension < 0.001:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)