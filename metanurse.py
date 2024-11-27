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
    if hypertension > 0.1 or intoxication > 0.05 or time_since_slept > 7:
        return 3  # sleep

    # Maintain alertness
    if alertness < 0.4 and intoxication < 0.02 and hypertension < 0.02:
        return 1  # drink coffee and work

    # Balance work and rest
    if time_elapsed > 10 and work_done < 0.6:
        return 3  # sleep

    # Avoid unnecessary actions
    if (
        work_done < 0.4
        and alertness > 0.3
        and intoxication < 0.02
        and hypertension < 0.02
    ):
        return 2  # drink beer and work

    return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)