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

    # Aggressively prioritize sleep if health metrics are concerning
    if (
        hypertension > 0.005
        or intoxication > 0.000001
        or time_since_slept > 0.1
        or alertness < 0.01
    ):
        return 3

    # Use coffee sparingly if alertness is low and health is not critical
    if alertness < 0.03 and intoxication < 0.000001 and hypertension < 0.002:
        return 1

    # Avoid beer unless absolutely necessary
    if alertness < 0.01 and intoxication < 0.000001 and hypertension < 0.002:
        return 2

    # Default to just working
    return 0


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)