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

    # Prioritize health
    if (
        hypertension > 0.5
        or intoxication > 0.03
        or time_since_slept > 10
        or alertness < 0.1
    ):
        return 3  # sleep

    # Maintain alertness and productivity
    if alertness < 0.3 and intoxication < 0.03 and hypertension < 0.3:
        return 1  # drink coffee and work

    # Boost productivity if not too intoxicated
    if work_done < 0.3 and intoxication < 0.03 and hypertension < 0.3:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)