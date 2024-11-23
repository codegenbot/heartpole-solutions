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

    if (
        time_since_slept > 3
        or alertness < 0.2
        or hypertension > 0.3
        or intoxication > 0.04
    ):
        return 3  # sleep
    elif alertness < 0.4 and intoxication < 0.02:
        return 1  # drink coffee and work
    elif work_done < 0.7 and intoxication < 0.02 and alertness > 0.3:
        return 0  # just work
    else:
        return 3  # fallback to sleep if conditions are not met


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)