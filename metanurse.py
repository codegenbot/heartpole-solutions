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
        hypertension > 0.6
        or intoxication > 0.02
        or time_since_slept > 8
        or alertness < 0.2
    ):
        return 3  # sleep

    # Moderate health conditions: avoid alcohol, use coffee if needed
    if alertness < 0.4 and intoxication < 0.01 and hypertension < 0.4:
        return 1  # drink coffee and work

    # If health is okay, focus on work
    if work_done < 0.4 and intoxication < 0.01 and hypertension < 0.4:
        return 0  # just work

    return 3  # default to sleep if unsure


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)