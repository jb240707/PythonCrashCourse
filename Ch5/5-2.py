#Series of conditional tests

vendor = "juniper"

print("Is vendor == 'juniper'? I predict True.")
print(vendor == 'juniper')

print("\nIs vendor == 'cisco'? I predict False.")
print(vendor == 'cisco')

print(vendor.lower() == 'juniper')



#Create list of switches and check whether value is in list.
switches_run = ['juniper', 'cisco', 'hp', 'meraki']

'juniper' in switches_run

'brocade' in switches_run


#Create multiple math condition comparisons to check for inequality.
dude_0 = 29
dude_1 = 45

dude_0 <= 30 and dude_1 <= 30
dude_0 <= 30 or dude_1 <= 30

dude_1 = 28

dude_0 <= 30 and dude_1 <= 30


#Check whether a value is not in a list. 
switches_run = ['juniper', 'cisco', 'hp', 'meraki']
switch = 'brocade'

if switch not in switches_run:
    print(switch.title() + " isn't widely used for campus LAN switching.")


#Use lower() function in for loop. 
switches_run = ['juniper', 'cisco', 'hp', 'meraki']


for switch in switches_run:
    if switch == 'hp':
        print(switch.upper())
    else:
        print(switch.title())