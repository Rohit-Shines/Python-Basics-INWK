class OSPF_database:
  def init(self,dtype,id,Adv_rtr,seq,Age,Opt,Cksum,len):
    self.dtype=dtype
    self.id=id
    self.Adv_rtr=Adv_rtr
    self.seq=seq
    self.Age=Age
    self.Opt=Opt
    self.CKsum=Cksum
    self.len=len
  def lsatype(self):
    if self.dtype=='ASBRSum':
      print("LSA type 5")
    elif self.dtype=='Summary':
      print("LSA type 3")
    elif self.dtype=='Network':
      print("LSA type 2")
    elif self.dtype=='Router':
      print("LSA type 1")
    else:
      print(" LSA type 4")



data=OSPF_database('ASBRSum','2.2.2.2','1.1.1.1','0x800003',1322,'0x22','0x726',28)
data.lsatype()