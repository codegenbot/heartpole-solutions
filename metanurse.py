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
        hypertension > 0.1
        or intoxication > 0.0003
        or time_since_slept > 0.8
        or alertness < 0.1
    ):
        return 3  # sleep

    # Only drink coffee if it won't exacerbate health issues and will boost alertness
    if alertness < 0.2 and intoxication < 0.0003 and hypertension < 0.03:
        return 1  # drink coffee and work

    # Avoid beer if it could exacerbate health issues and only if it will boost work done
    if work_done < 0.2 and intoxication < 0.0003 and hypertension < 0.03:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)