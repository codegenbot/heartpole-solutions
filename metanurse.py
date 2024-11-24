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

    # Critical health conditions
    if (
        hypertension > 0.6
        or intoxication > 0.2
        or time_since_slept > 20
        or alertness < 0.1
    ):
        return 3  # sleep

    # High hypertension or intoxication, prioritize sleep
    if hypertension > 0.4 or intoxication > 0.1:
        return 3  # sleep

    # Moderate alertness and safe health conditions
    if alertness < 0.6 and intoxication < 0.1 and hypertension < 0.4:
        return 1  # drink coffee and work

    # Low work done and safe health conditions
    if work_done < 0.6 and intoxication < 0.1 and hypertension < 0.4:
        return 0  # just work

    return 3  # default to sleep if unsure


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)