import json

with open (r'C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab4\JSON\sample_data.json') as ourfile:
    ourdata = json.load(ourfile)

ourinterfaces = ourdata["imdata"]

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")


for item in ourinterfaces:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(dn + "                              " + speed + "   " + mtu)