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

    # Prioritize sleep for critical health conditions
    if (
        hypertension > 0.55
        or intoxication > 0.015
        or time_since_slept > 3.5
        or alertness < 0.05
    ):
        return 3  # sleep

    # Adjust thresholds for coffee and beer
    if alertness < 0.15 and intoxication < 0.01 and hypertension < 0.45:
        return 1  # drink coffee and work
    elif work_done < 0.15 and intoxication < 0.01 and hypertension < 0.45:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)