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

    # Aggressively prioritize sleep for health issues
    if (
        hypertension > 0.3
        or intoxication > 0.002
        or time_since_slept > 2.0
        or alertness < 0.1
    ):
        return 3  # sleep

    # Only drink coffee if it won't exacerbate health issues
    if alertness < 0.3 and intoxication < 0.002 and hypertension < 0.2:
        return 1  # drink coffee and work

    # Avoid beer if it could exacerbate health issues
    if work_done < 0.3 and intoxication < 0.002 and hypertension < 0.2:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)