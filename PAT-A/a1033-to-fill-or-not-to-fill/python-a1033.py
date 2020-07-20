
capacity, distance, avg, count = '50 1300 12 8'.split() 
capacity, distance, avg, count = float(capacity), float(distance), float(avg), int(count)
stations = [tuple(map(float, i.split())) for i in ['6.00 1250','7.00 600','7.00 150','7.10 0','7.20 200','7.50 400','7.30 1000','6.85 300']]
stations.append((0.0, distance))
# stations = [tuple(map(float, input().split())) for i in range(count)]
stations = sorted(stations, key=lambda x: (x[1], x[0]))

total = 0.0
current_capacity = 0.0
current_distance = 0.0

if stations[0][1]:
    print('The maximum travel distance = 0.00')
else:
    current_price = stations[0][0]

for price, distance in stations[1:]:
    if current_price <= price:
        # 如果当前油价最便宜，那就将油箱加满
        total += current_price * (capacity-current_capacity)
    else:
        # 如果当前油价不如下一站便宜，那就加到保证能到下一站的油
        total += current_price * (distance-current_distance)/avg

    print(price, distance, total)
