python
omløpsmidler = 300000
kortsiktig_gjeld = 150000
varelager = 50000

likviditetsgrad_1 = omløpsmidler / kortsiktig_gjeld
likviditetsgrad_2 = (omløpsmidler - varelager) / kortsiktig_gjeld

print(f"Likviditetsgrad 1: {likviditetsgrad_1}")
print(f"Likviditetsgrad 2: {likviditetsgrad_2}")