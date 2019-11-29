# Do not print "maruti" from ["alto", "maruti", "ferrari"]
cars = ["alto", "maruti", "ferrari"]
for x in cars:
  if x == "maruti":
    continue
  print(x)
