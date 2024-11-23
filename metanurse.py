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

    if hypertension > 0.4 or intoxication > 0.005:
        return 3  # sleep to reduce hypertension and intoxication
    elif time_since_slept > 2.5 or alertness < 0.2:
        return 3  # sleep to regain alertness
    elif alertness < 0.4 and intoxication < 0.005 and hypertension < 0.3:
        return 1  # drink coffee and work to boost alertness
    elif work_done < 0.4 and intoxication < 0.005 and hypertension < 0.3:
        return 2  # drink beer and work to boost work done
    else:
        return 0  # just work


for _ in range(1000):
    observations = list(map(float, sys.stdin.readline().strip().split()))
    if len(observations) != 6:
        break
    action = choose_action(observations)
    print(action)