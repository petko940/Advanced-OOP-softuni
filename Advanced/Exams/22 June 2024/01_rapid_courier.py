from collections import deque

weight_packages = deque([int(x) for x in input().split()])
capacities_couriers = deque([int(x) for x in input().split()])

total_weight = 0

while weight_packages and capacities_couriers:
    last_package = weight_packages.pop()
    first_courier = capacities_couriers.popleft()

    if first_courier >= last_package:
        total_weight += last_package
        if first_courier > last_package:
            first_courier -= 2 * last_package
            if first_courier > 0:
                capacities_couriers.append(first_courier)

    else:
        last_package -= first_courier
        weight_packages.append(last_package)
        total_weight += first_courier

print(f"Total weight: {total_weight} kg")

if weight_packages:
    print(f"Unfortunately, there are no more available couriers to deliver "
          f"the following packages: {', '.join([str(x) for x in weight_packages])}")
elif capacities_couriers:
    print(f"Couriers are still on duty: {', '.join([str(x) for x in capacities_couriers])} "
          f"but there are no more packages to deliver.")
else:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
