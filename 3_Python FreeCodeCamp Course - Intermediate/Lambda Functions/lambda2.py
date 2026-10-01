points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)
points2D_sorted2 = sorted(points2D, key=lambda x: x[1]) #sort on basis of second element of each pair


print(points2D)
print(points2D_sorted)
print(points2D_sorted2)