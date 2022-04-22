# Objective: To understand SD-WAN process through Python programing. Proposed date of completion is coming Friday.
# Background: In conventional WAN links, the secondary transport link (Link B) usually sits idle without any traffic using it until Link A fails. With SD-WAN, options of application load-balancing over multiple links in a hybrid environment becomes possible. Hybrid WAN approach is enabled that uses bandwidth from both links as an A + A or an Active/Active scenario. Various options are possible for example weighted per-session round-robin is also configurable, application pinning, or forcing an application to take a specific transport. An application-aware routing or SLA-compliant routing for jitter, loss, and delay can be therefore implemented. An SLA determines if the application is adhering to that policy, and performing properly, or if it is experiencing some sort of detriment such as jitter, loss, or delay. Then application can be routed to another transport that will ensure SLA compliance
# Proposed Scenario:
# A scenario such as the following with some exceptions. You can avoid having a vManage that connects to the remote sites to avoid teaching student to connect the central control to the remote sites. Instead, the programs you write will work on remote sites.


def remotesite(InternetSpeed, MultiprotocolLabelSwitch, LongTermEvolution):
    if (InternetSpeed == 0 or MultiprotocolLabelSwitch == 0 or LongTermEvolution == 0):
        if (InternetSpeed == 0):
            print("path 1 is down")
            print("path 2 will carry the data of {} with 200ms delay, 3% loss and 10 ms jitter".format(MultiprotocolLabelSwitch))
            print("path 3 will carry the data of {} with 140ms delay, 1% loss and 10 ms jitter".format(LongTermEvolution))
        elif (MultiprotocolLabelSwitch == 0):
            print("path 2 is down")
            print("path 1 will carry the data of {} with 10ms delay, 0% loss and 5 ms jitter".format(InternetSpeed))
            print("path 3 will carry the data of {} with 140ms delay, 1% loss and 10 ms jitter".format(LongTermEvolution))
        elif (LongTermEvolution == 0):
            print("path 3 is down")
            print("path 1 will carry the data of {} with 10ms delay, 0% loss and 5 ms jitter".format(InternetSpeed))
            print("path 2 will carry the data of {} with 200ms delay, 3% loss and 10 ms jitter".format(MultiprotocolLabelSwitch))
    else:
        print("All the path are up and working fine")
        print("path 1 will carry the data of {} with 10ms delay, 0% loss and 5 ms jitter".format(InternetSpeed))
        print("path 2 will carry the data of {} with 200ms delay, 3% loss and 10 ms jitter".format(MultiprotocolLabelSwitch))
        print("path 3 will carry the data of {} with 140ms delay, 1% loss and 10 ms jitter".format(LongTermEvolution))


def datacenter(InternetSpeed, MultiprotocolLabelSwitch, LongTermEvolution):
    if (InternetSpeed == 0 or MultiprotocolLabelSwitch == 0 or LongTermEvolution == 0):
        if (InternetSpeed == 0):
            print("As path 1 is down, other two paths are the available links:")
            destination_mpls = MultiprotocolLabelSwitch - (MultiprotocolLabelSwitch * 0.03)
            print("path 2 has carried the data of {} with 200ms delay and 10 ms jitter at the datacenter".format(
                destination_mpls))
            destination_lte = LongTermEvolution - (LongTermEvolution * 0.01)
            print("path 3 has carried the data of {} with 140ms delay and 10 ms jitter at the datacenter".format(
                destination_lte))
        elif (MultiprotocolLabelSwitch == 0):
            print("As path 2 is down, other two paths are the available links:")
            print(
                "path 1 has carried the data of {} with 10ms delay and 5 ms jitter at the datacenter".format(InternetSpeed))
            destination_lte = LongTermEvolution - (LongTermEvolution * 0.01)
            print("path 3 has carried the data of {} with 140ms delay and 10 ms jitter at the datacenter".format(
                destination_lte))
        elif (LongTermEvolution == 0):
            print("As path 3 is down, other two paths are the available links:")
            print(
                "path 1 has carried the data of {} with 10ms delay and 5 ms jitter at the datacenter".format(InternetSpeed))
            destination_mpls = MultiprotocolLabelSwitch - (MultiprotocolLabelSwitch * 0.03)
            print("path 2 has carried the data of {} with 200ms delay and 10 ms jitter at the datacenter".format(
                destination_mpls))

    else:
        print("The data has reached the destionation from the three paths")
        print("path 1 has carried the data of {} with 10ms delay and 5 ms jitter at the datacenter".format(InternetSpeed))
        destination_mpls = MultiprotocolLabelSwitch - (MultiprotocolLabelSwitch * 0.03)
        print("path 2 has carried the data of {} with 200ms delay and 10 ms jitter at the datacenter".format(
            destination_mpls))
        destination_lte = LongTermEvolution - (LongTermEvolution * 0.01)
        print("path 3 has carried the data of {} with 140ms delay and 10 ms jitter at the datacenter".format(
            destination_lte))


def run_SDWAN_Architecture(internet, mpls, lte):
    remotesite(internet_user, mpls_user, lte_user)
    datacenter(internet_user, mpls_user, lte_user)


internet_user = int(input("data carried by internet connection "))
mpls_user = int(input("data carried by MultiprotocolLabelSwitch  path"))
lte_user = int(input("data carried by long-term-evolution path"))
