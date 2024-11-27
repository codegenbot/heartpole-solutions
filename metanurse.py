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

    if hypertension > 0.1 or intoxication > 0.05 or time_since_slept > 7:
        return 3  # sleep

    if alertness < 0.5 and intoxication < 0.02 and hypertension < 0.02:
        return 1  # drink coffee and work

    if (
        work_done < 0.4
        and intoxication < 0.02
        and hypertension < 0.02
        and alertness > 0.3
    ):
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)