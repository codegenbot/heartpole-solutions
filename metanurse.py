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

    if alertness < 0.1 or hypertension > 0.25 or intoxication > 0.001:
        return 3  # sleep
    elif alertness < 0.3 and intoxication < 0.001 and hypertension < 0.2:
        return 1  # drink coffee and work
    elif work_done < 0.3 and intoxication < 0.001 and hypertension < 0.2:
        return 2  # drink beer and work
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)