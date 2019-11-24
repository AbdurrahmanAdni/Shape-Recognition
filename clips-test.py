import clips
env = clips.Environment()
# Assert the first ordeded-fact as string so its template can be retrieved
# fact_string = "(ordered-fact 1 2 3)"
# fact = env.assert_string(fact_string)
# template = fact.template
# assert template.implied == True
# new_fact = template.new_fact()
# new_fact.extend((3, 4, 5))
# new_fact.assertit()

# factlist = []
# for fact in env.facts():
#     factlist.append(fact)

# for x in factlist:
#     print(x)

template_string = """
(deftemplate template-fact
(slot template-slot (type SYMBOL)))
"""
env.build(template_string)
template = env.find_template('template-fact')
new_fact = template.new_fact()
new_fact['template-slot'] = clips.Symbol('a-symbol')
new_fact.assertit()
for fact in env.facts():
    print("badoor")
    print(fact)