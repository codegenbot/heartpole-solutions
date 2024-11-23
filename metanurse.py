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

    if hypertension > 0.3 or intoxication > 0.0005:
        return 3  # sleep
    elif time_since_slept > 0.7 or alertness < 0.3:
        return 3  # sleep
    elif alertness < 0.5 and intoxication < 0.0005 and hypertension < 0.3:
        return 1  # drink coffee and work
    elif (
        work_done < 0.4
        and intoxication < 0.0005
        and hypertension < 0.3
        and time_elapsed < 0.6
    ):
        return 2  # drink beer and work
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)