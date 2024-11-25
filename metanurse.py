import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate response to critical health metrics
    if hypertension > 0.18 or intoxication > 0.18 or time_since_slept > 6:
        return 3  # sleep to tackle serious issues

    # Sleep if severely lacking alertness
    if alertness < 0.6:
        return 3

    # Use coffee only if safe from high hypertension and requiring alertness
    if alertness < 0.75 and hypertension < 0.12:
        return 1  # boost alertness safely

    # Ideal working conditions
    if alertness >= 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # continue working efficiently

    # Relax conditionally when workload is significantly lower
    if work_done < 0.6 and intoxication < 0.1:
        return 2  # mild relaxation with beer

    return 0  # default to just work when other conditions are stable


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)