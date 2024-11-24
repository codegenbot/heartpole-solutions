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

    # Critical health conditions: always sleep
    if (
        hypertension > 0.5
        or intoxication > 0.1
        or time_since_slept > 15
        or alertness < 0.1
    ):
        return 3  # sleep

    # If alertness is low but not critical, use coffee
    if alertness < 0.3 and intoxication < 0.1 and hypertension < 0.3:
        return 1  # drink coffee and work

    # If work is not progressing well and health is okay, use beer
    if work_done < 0.3 and intoxication < 0.1 and hypertension < 0.3:
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)