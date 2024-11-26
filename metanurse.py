import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Address severe health issues immediately
    if hypertension >= 0.08 or intoxication >= 0.2:
        return 3  # Must sleep if health risks are high

    # Prioritize rest to maintain balance
    if alertness < 0.4 or time_since_slept >= 7:
        return 3  # Sleep if alertness is low or sleep deprivation

    # Use caffeine strategically
    if 0.4 <= alertness < 0.7 and hypertension < 0.03:
        return 1  # Drink coffee and work for an optimal boost

    # Avoid alcohol unless alertness is very high
    if alertness >= 0.9 and intoxication < 0.1:
        return 2  # Drink beer and work for relaxation if safe

    # Work under safe and productive conditions
    return 0  # Default: just work if all conditions are adequate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)