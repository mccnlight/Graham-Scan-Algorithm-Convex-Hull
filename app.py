import math
import matplotlib.pyplot as plt


# Function to calculate the polar angle between p0 and p1, used for sorting points
def polar_angle(p0, p1):
    delta_x = p1[0] - p0[0]
    delta_y = p1[1] - p0[1]
    return math.atan2(delta_y, delta_x)  # Returns angle in radians


# Function to calculate the Euclidean distance between points p0 and p1
def distance(p0, p1):
    x1, y1, x2, y2 = *p0, *p1
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Function to determine the orientation of the triplet (p0, p1, p2)
def orientation(p0, p1, p2):
    x1, y1, x2, y2, x3, y3 = *p0, *p1, *p2
    x = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    if x > 0:
        return 1  # Counter-clockwise turn
    elif x < 0:
        return -1  # Clockwise turn
    else:
        return 0  # Collinear points


# Main function to compute the convex hull of a set of points
def convex_hull(points):
    if len(points) < 3:  # Check if a convex hull can be formed
        return None
    points = list(set(points))  # Remove duplicate points
    # Start with the point with the lowest y-coordinate, breaking ties by x-coordinate
    p0 = min(points, key=lambda p: (p[1], p[0]))
    # Sort points by polar angle with p0 and distance from p0 in case of ties
    points.sort(key=lambda p: (polar_angle(p0, p), distance(p0, p)))

    hull = []  # Initialize an empty stack to hold points on the hull
    for i in range(len(points)):
        # Remove last point from hull if it does not form a counter-clockwise turn
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])  # Add current point to the hull
    return hull


# Function to plot the points and the convex hull
def plot_hull(points, hull):
    # Separate x and y coordinates of points
    x, y = zip(*points)
    plt.scatter(x, y, label='Points')  # Plot all points

    # Close the convex hull loop by appending the first hull point at the end
    hull.append(hull[0])
    hx, hy = zip(*hull)
    plt.plot(hx, hy, color='r', label='Convex Hull')  # Draw the convex hull as a polygon

    plt.legend()
    plt.show()


# Define points and calculate convex hull
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3), (0, 2), (4, 2)]
hull = convex_hull(points)

# Display the convex hull and plot if a hull is formed
if hull is not None:
    print("Convex hull: ", hull)
    plot_hull(points, hull)
else:
    print("No convex hull can be formed with fewer than 3 points!")
