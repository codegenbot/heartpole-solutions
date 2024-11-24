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

    # Critical health conditions
    if (
        hypertension > 0.7
        or intoxication > 0.3
        or time_since_slept > 24
        or alertness < 0.05
    ):
        return 3  # sleep

    # Moderate alertness and health conditions
    if alertness < 0.3 and intoxication < 0.1 and hypertension < 0.5:
        return 1  # drink coffee and work

    # Low work done and safe health conditions
    if work_done < 0.3 and intoxication < 0.1 and hypertension < 0.5:
        return 0  # just work

    # Low alertness and safe health conditions
    if alertness < 0.2 and intoxication < 0.1 and hypertension < 0.5:
        return 2  # drink beer and work

    return 0  # default to just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)