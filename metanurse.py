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

    # Always prioritize sleep if health metrics are critical
    if (
        hypertension > 0.6
        or intoxication > 0.2
        or time_since_slept > 20
        or alertness < 0.1
    ):
        return 3  # sleep

    # Avoid alcohol if it could worsen health metrics
    if intoxication < 0.1 and hypertension < 0.4 and alertness < 0.3:
        return 1  # drink coffee and work

    # Just work if health metrics are stable and alertness is acceptable
    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)