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
        hypertension > 0.02
        or intoxication > 0.000003
        or time_since_slept > 0.3
        or alertness < 0.07
    ):
        return 3  # sleep

    # Drink coffee if alertness is very low and health conditions are safe
    if alertness < 0.1 and intoxication < 0.000003 and hypertension < 0.005:
        return 1  # drink coffee and work

    # Avoid beer if a significant amount of work is already done
    if (
        work_done < 0.05
        and intoxication < 0.000003
        and hypertension < 0.005
        and work_done < 0.4
    ):
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)