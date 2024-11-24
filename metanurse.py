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

    # Aggressively prioritize sleep for critical health metrics
    if (
        hypertension > 0.005
        or intoxication > 0.000005
        or time_since_slept > 0.05
        or alertness < 0.005
    ):
        return 3  # sleep

    # If alertness is low and not intoxicated or hypertensive, drink coffee
    if alertness < 0.1 and intoxication < 0.000005 and hypertension < 0.0005:
        return 1  # drink coffee and work

    # If work done is significantly low and not intoxicated or hypertensive, drink beer
    if work_done < 0.05 and intoxication < 0.000005 and hypertension < 0.0005:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)