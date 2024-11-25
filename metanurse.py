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

    # Prioritize sleep for critical health conditions
    if (
        hypertension > 0.6
        or intoxication > 0.01
        or time_since_slept > 7
        or alertness < 0.2
    ):
        return 3  # sleep

    # Use coffee to boost alertness if safe
    if alertness < 0.4 and intoxication < 0.01 and hypertension < 0.4:
        return 1  # drink coffee and work

    # Avoid alcohol if productivity is low or health metrics are concerning
    if work_done < 0.4 and intoxication < 0.01 and hypertension < 0.4:
        return 0  # just work

    return 0  # default to just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)