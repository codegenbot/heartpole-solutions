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

    # Strict health checks
    if (
        hypertension > 0.15
        or intoxication > 0.005
        or time_since_slept > 10
        or alertness < 0.15
    ):
        return 3  # sleep

    # Moderate alertness boost with coffee
    if alertness < 0.5 and intoxication < 0.002 and hypertension < 0.03:
        return 1  # drink coffee and work

    # Moderate work boost with beer
    if work_done < 0.5 and intoxication < 0.002 and hypertension < 0.03:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)