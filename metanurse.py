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

    # Prioritize sleep for health concerns
    if (
        hypertension > 0.1
        or intoxication > 0.0001
        or time_since_slept > 0.6
        or alertness < 0.2
    ):
        return 3  # sleep

    # Enhance alertness with coffee if not too intoxicated
    if alertness < 0.4 and intoxication < 0.0001 and hypertension < 0.1:
        return 1  # drink coffee and work

    # Use beer to boost work if conditions are right
    if (
        work_done < 0.3
        and intoxication < 0.0001
        and hypertension < 0.1
        and time_elapsed < 0.5
    ):
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)