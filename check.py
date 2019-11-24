from clips import *

# Initialize
env = Environment()

# Load rule
rule = """
(defrule add
    (number ?x1)
    (number ?x2)
    =>
    (assert (number_result (+ ?x1 ?x2)))
)
"""
env.build(rule)

# Assert fact
env.assert_string('(number 1)')
env.assert_string('(number 5)')

# Run
env.run()

# Check facts
for fact in env.facts():
    # <class 'clips.facts.ImpliedFact'>
    print(fact)

    # Convert to string
    print(str(fact))

