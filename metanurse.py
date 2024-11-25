import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.15 or intoxication > 0.07 or alertness < 0.5:
        return 3  # Prioritize health by sleeping more frequently
    if alertness < 0.75 and time_since_slept > 4:
        return 1  # Use coffee to boost alertness if not recently rested
    if work_done < time_elapsed * 0.05 and hypertension < 0.08:
        return 2  # Maintain moderate productivity with relaxation
    return 0  # Default to just work if conditions are stable


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)