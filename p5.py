import random

def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def total_distance(route, cities):
    return sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route) - 1))

def hill_climbing_tsp(cities, max_iters):
    route = list(range(len(cities)))
    random.shuffle(route)
    cost = total_distance(route, cities)
    
    for _ in range(max_iters):
        new_route = route.copy()
        i, j = sorted(random.sample(range(len(cities)), 2))
        new_route[i:j+1] = reversed(new_route[i:j+1])
        
        new_cost = total_distance(new_route, cities)
        if new_cost < cost:
            route, cost = new_route, new_cost
            
    return route, cost

# Example Usage
cities = [(0, 0), (1, 2), (3, 1), (5, 3), (6, 0)]
best_route, best_cost = hill_climbing_tsp(cities, 10000)
print("Best Route:", best_route)
print("Best Cost:", best_cost)
