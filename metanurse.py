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
        hypertension > 0.2
        or intoxication > 0.0003
        or time_since_slept > 0.8
        or alertness < 0.05
    ):
        return 3  # sleep

    # Drink coffee if alertness is low and health conditions are safe
    if alertness < 0.15 and intoxication < 0.0001 and hypertension < 0.1:
        return 1  # drink coffee and work

    # Avoid beer if a significant amount of work is already done
    if (
        work_done < 0.1
        and intoxication < 0.0001
        and hypertension < 0.1
        and work_done < 0.7
    ):
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)