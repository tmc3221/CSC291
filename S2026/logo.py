import math

tests = int(input())

for i in range(tests):
    n = int(input())
   
    distance_x = 0
    distance_y = 0
    pointing = 0

    for j in range(n):
        direction, distance = input().split()
        distance = int(distance)

        if direction == 'fd':
            distance_x = distance_x + math.cos(math.radians(pointing)) * distance
            distance_y = distance_y + math.sin(math.radians(pointing)) * distance
        elif direction == 'bk':
            distance_x = distance_x - math.cos(math.radians(pointing)) * distance
            distance_y = distance_y - math.sin(math.radians(pointing)) * distance
        elif direction == 'lt':
            pointing = pointing - (distance % 360)
        elif direction == 'rt':
            pointing = pointing + (distance % 360)

    print(round(math.sqrt(distance_x ** 2 + distance_y ** 2)))
