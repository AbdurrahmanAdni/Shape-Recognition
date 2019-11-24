import clips
env = clips.Environment()
# Assert the first ordeded-fact as string so its template can be retrieved
fact_string = "(ordered-fact 1 2 3)"
fact = env.assert_string(fact_string)
template = fact.template
assert template.implied == True
new_fact = template.new_fact()
new_fact.extend((3, 4, 5))
new_fact.assertit()

for fact in env.facts():
    print(fact)