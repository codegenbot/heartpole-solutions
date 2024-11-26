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

    # Aggressively prioritize sleep for health
    if (
        hypertension > 0.002
        or intoxication > 0.00000003
        or time_since_slept > 0.15
        or alertness < 0.03
    ):
        return 3  # sleep

    # Ensure alertness with coffee
    if alertness < 0.6 and intoxication < 0.00000003 and hypertension < 0.002:
        return 1  # drink coffee and work

    # Balance work and rest with beer
    if work_done < 0.0000002 and intoxication < 0.00000003 and hypertension < 0.002:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)