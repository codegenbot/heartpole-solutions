import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if reaching or risk to exceed critical levels
    if alertness < 0.6 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept >= 6:
        return 3  # Must sleep

    # Prioritize work if highly alert and health indicators are optimal
    if alertness >= 0.9 and hypertension < 0.35 and intoxication < 0.1:
        return 0  # Just work

    # Regain alertness with coffee if it's low, and it's safe to do so
    if alertness <= 0.7 and hypertension <= 0.45:
        return 1  # Drink coffee and work

    # Use beer to relax if slightly needed but intoxication should be controlled
    if alertness < 0.6 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 0  # Continue working safely if indicators are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)