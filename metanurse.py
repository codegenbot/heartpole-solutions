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
        hypertension > 0.05
        or intoxication > 0.000005
        or time_since_slept > 1.5
        or alertness < 0.03
    ):
        return 3  # sleep

    # Ensure alertness and avoid over-intoxication
    if alertness < 0.4 and intoxication < 0.000005 and hypertension < 0.04:
        return 1  # drink coffee and work

    # Balance work and rest
    if work_done < 0.000005 and intoxication < 0.000005 and hypertension < 0.04:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)