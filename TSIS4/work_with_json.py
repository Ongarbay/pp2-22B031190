import json
with open("sample-data.json", "r") as read_file:
    data = json.load(read_file)
    print("Interface Status")
    print("================================================================================")
    print("DN                                                       Description           Speed        MTU  ")
    print("--------------------------------------------------   --------------------      ------      ------")
    for s in range(18):
        for x, y in data["imdata"][s]['l1PhysIf']["attributes"].items():
            if x == 'dn':
                print(y, end="                                    ")
            if x == "mtu":
                print(y, end="")
            if x == "fecMode":
                print(y, end="       ")
        print("\n")
