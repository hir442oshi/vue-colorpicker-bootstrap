import pandas as pd

def check_policy_compliance(content, policy_rules):
    # Benchmark content against aiEDU literacy standards
    violations = []
    for rule in policy_rules:
        if rule not in content:
            violations.append(rule)
    return violations