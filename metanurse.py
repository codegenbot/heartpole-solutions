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

    # Prioritize sleep for health issues
    if hypertension > 0.5 or intoxication > 0.01:
        return 3  # sleep
    elif time_since_slept > 4 or alertness < 0.05:
        return 3  # sleep

    # Only drink coffee if it won't exacerbate health issues
    if alertness < 0.2 and intoxication < 0.01 and hypertension < 0.4:
        return 1  # drink coffee and work

    # Avoid beer if it could exacerbate health issues
    if work_done < 0.2 and intoxication < 0.01 and hypertension < 0.4:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)