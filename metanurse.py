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

    if (
        time_since_slept > 4
        or alertness < 0.2
        or hypertension > 0.5
        or intoxication > 0.05
    ):
        return 3  # sleep
    elif alertness < 0.4 and intoxication < 0.03 and hypertension < 0.3:
        return 1  # drink coffee and work
    elif work_done < 0.7 and intoxication < 0.03 and alertness > 0.3:
        return 0  # just work
    elif work_done < 0.6 and intoxication < 0.03 and alertness > 0.4:
        return 2  # drink beer and work (if work is lagging and conditions are safe)
    else:
        return 3  # fallback to sleep if conditions are uncertain


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)