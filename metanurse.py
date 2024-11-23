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
        time_since_slept > 6
        or alertness < 0.1
        or hypertension > 0.65
        or intoxication > 0.1
    ):
        return 3  # sleep
    elif alertness < 0.2 and intoxication < 0.03 and hypertension < 0.4:
        return 1  # drink coffee and work
    elif work_done < 0.2 and intoxication < 0.03 and hypertension < 0.4:
        return 0  # just work, avoid beer
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)