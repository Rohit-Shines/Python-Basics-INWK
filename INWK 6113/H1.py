# Question 1
# With Python simulate a scenario by using writing a class and methods with appropriate
# attributes. This scenario should assume 5 equal cost path options from the same source to the
# same destination to load balance in a Round Robin basis. You should make a test plan and, in the
# result, should prove that RIP enables load balancing only with equal cost paths.

def RoutingInformationProtocol(routes, requests):

  v = routes[0]
  for i in routes:
    if v != i:
      print("LB will not work")
  print("LB will work")
  s = 1


  for i in requests:
    print("Route ", s , "Adapting the Request ", i)
    s += 1
RoutingInformationProtocol([4,4,4,4], [2,4,1,7])



# Question 2:
# (a) Write a class for electing BDR and DR and replacement of DR by BDR.
# (b) Write test cases
# (c) Write Result

def Replacement():
  database = {"R1":"3.3.3.3", "R2":"8.8.8.8", "R3":"2.2.2.2", "R4":"11.11.11.11", "R5":"2.2.2.2"}
  DR = ""
  BDR = ""
  for key,val in database.items():
    if val > DR:
      DR = key
    elif val > BDR:
      BDR = key
  print("BDR", BDR)
  print("DR", DR)
Replacement()