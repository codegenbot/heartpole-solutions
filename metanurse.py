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
        hypertension > 0.1
        or intoxication > 0.000001
        or time_since_slept > 1.5
        or alertness < 0.1
    ):
        return 3  # sleep

    # If not in critical health condition, consider productivity
    if alertness < 0.3 and intoxication < 0.000001 and hypertension < 0.1:
        return 1  # drink coffee and work

    if work_done < 0.000001 and intoxication < 0.000001 and hypertension < 0.1:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)