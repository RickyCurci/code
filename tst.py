def football_points(wins, draws, losses):
	points = []

	points.append(wins * 3)
	points.append(draws * 1)
	points.append(losses * 0)

	print(points)

	for point in points:
		if points.index(point) == 2:
			break

		result = point + point[points.index(point) + 1]

		print(result)
		

football_points(3, 2, 1)
