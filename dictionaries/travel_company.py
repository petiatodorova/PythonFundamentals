'''Athens:bus-40,airplane-300,train-150
Athens:minibus-8,airplane-350
Warsaw:bus-30,train-150,airplane-120
ready'''
line = input().split(":")

town_transport = {}

while not line[0] == "ready":
    town = line[0]
    transport = line[1].split(",")
    if town not in town_transport.keys():
        town_transport[town] = {}
    for item in transport:
        item.split("-")
        key = item[0]
        value = int(item[1])
        if key not in town_transport[town].keys():
            town_transport[town][key] = {}
        town_transport[town][key] += value
    line = input().split(":")

print(town_transport)