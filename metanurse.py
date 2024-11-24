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

    # Prioritize sleep if health metrics are concerning
    if (
        hypertension > 0.05
        or intoxication > 0.00001
        or time_since_slept > 0.3
        or alertness < 0.03
    ):
        return 3

    # Use coffee if alertness is low and health is not critical
    if alertness < 0.1 and intoxication < 0.000005 and hypertension < 0.02:
        return 1

    # Avoid beer unless absolutely necessary
    if alertness < 0.03 and intoxication < 0.000005 and hypertension < 0.02:
        return 2

    # Default to just working
    return 0


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)