# Preferably, try to use classes wherever possible.
# Q.1 (a) Write a program in Python with well commented quote for the algorithm that breaks a loop in
# BGP
# (b) Write test cases to test your code
# (c) By following your testing strategy, show the successful results.
# Q. 2 (a) Program the route preference criteria of BGP in Python with well commented quote.
# (b) Write test cases to test your code
# (c) By following your testing strategy, show the successful results.
# Q.3 (a) Program the behaviour of penalty due to route flapping because of i) route being available or not
# and ii) a route being there with changing cost by using the formula given the video of route dampening.
# (b) Write test cases to test your code
# (c) By following your testing strategy, show the successful results.
# Q. 4 (a) Program the scenario where TTL of IP is copied into MPLS packet at the Ingress LSR and copy
# back the MPLS TTL back to IP TTL at the Egress LSR (with both TTL propagation on and blocked) .
# (b) Write test cases to test your code
# (c) By following your testing strategy, show the successful results.


n =int(input(" Enter the routers' count in the topology:"))
routers = dict(input("Enter THE  hostname & (ebgp/ibgp): ").split() for _ in range(n))
for key,value in routers.items():
  print(key, '->', value)
  if value == "EBGP":
    break



import random
class Route_Preference:
    def _init_(self,AD1,AD2,AD3,AD4,AD5):
        self.AD1=AD1
        self.AD2=AD2
        self.AD3=AD3
        self.AD4=AD4
        self.AD5=AD5

    def path_1(self):
        print("Path 1 is used having cost",self.AD1)
    def path_2(self):
        print("Path 2 is used having cost",self.AD2)
    def path_3(self):
        print("Path 3 is used having cost",self.AD3)
    def path_4(self):
        print("Path 4 is used having cost",self.AD4)
    def path_5(self):
        print("Path 5 is used having cost",self.AD5)

path1=int(input("Enter the AD of path 1:"))
path2=int(input("Enter the AD of path 2:"))
path3=int(input("Enter the AD of path 3:"))
path4=int(input("Enter the AD of path 4:"))
path5=int(input("Enter the AD of path 5:"))
min_AD=min(ADS)
R1=Route_Preference(path1,path2,path3,path4,path5)
if min_AD==path1:
  R1.path_1()
elif min_AD==path2:
  R1.path_2()
elif min_AD==path3:
  R1.path_3()
elif min_AD==path4:
  R1.path_4()
elif min_AD==path5:
  R1.path_5()
else:
  print("path was not chosen")

#problem 4
class MPLS:
    def _init_(self,ttl):
        self.ttl=ttl
        self.ipttl=0
    def mpls_ttl(self):
        return self.ttl
    def mpls_packet(self):
        print("TTL values in mpls are "+str(self.ttl)+" and "+str(self.ipttl))
    def ip_in_mpls(self,ipttl):
        self.ipttl=ipttl
class IP:
    def _init_(self,ttl):
        self.ttl=ttl
        self.mplsttl=0
    def IP_ttl(self):
        return self.ttl
    def ip_packet(self):
        print("TTL values in IP are "+str(self.ttl)+" and "+str(self.mplsttl))
    def mpls_in_ip(self,mplsttl):
        self.mplsttl=mplsttl