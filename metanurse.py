import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize resolving serious health issues
    if hypertension > 0.10 or intoxication > 0.07 or time_since_slept > 3:
        return 3  # sleep more aggressively to fix any health issue

    # Adjust alertness criteria
    if alertness < 0.5:
        return 3  # sleep if alertness is below a healthier threshold

    # Use coffee more conservatively
    if alertness < 0.7 and hypertension < 0.08:
        return 1  # drink coffee if moderately low alertness and hypertension is low

    # Optimize conditions for working with balanced thresholds
    if alertness >= 0.8 and hypertension < 0.04 and intoxication < 0.01:
        return 0  # prioritize working under nearly perfect conditions

    # Adjust criteria for relaxation
    if work_done < 0.2 and alertness > 0.6:
        if intoxication < 0.04:  # stricter condition for beer
            return 2  # beer for slight relaxation if conditions are favorable

    return 0  # default to working if no other action is clearly necessary

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)