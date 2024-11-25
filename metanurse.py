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
        hypertension > 0.002
        or intoxication > 0.0000003
        or time_since_slept > 0.6
        or alertness < 0.1
    ):
        return 3  # sleep

    # If alertness is low and conditions are safe, drink coffee
    if alertness < 0.4 and intoxication < 0.0000003 and hypertension < 0.0003:
        return 1  # drink coffee and work

    # If work is not done and conditions are safe, drink beer
    if work_done < 0.6 and intoxication < 0.0000003 and hypertension < 0.0003:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)