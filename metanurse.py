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
        hypertension > 0.2
        or intoxication > 0.0003
        or time_since_slept > 0.6
        or alertness < 0.2
    ):
        return 3  # sleep
    elif alertness < 0.6 and intoxication < 0.0002 and hypertension < 0.2:
        return 1  # drink coffee and work
    elif time_elapsed > 0.6 and work_done < 0.5:
        return 3  # sleep after a significant time elapsed and not much work done
    elif intoxication < 0.0001 and hypertension < 0.1 and time_elapsed > 0.4:
        return 2  # drink beer and work if conditions are safe
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)