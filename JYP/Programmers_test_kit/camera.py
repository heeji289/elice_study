#routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
#routes = [[-10,0], [-3,5], [-5,7], [9,11]] 

def solution(routes):

    #1. out point check and sort
    sorted_routes = sorted(routes, key=lambda x: x[1])

    #2. compare: in and out
    camera = 1
    out = sorted_routes[0][1]

    for i in range(1, len(routes)):
        if sorted_routes[i][0] > out:
            camera += 1
            out = sorted_routes[i][1]

    return camera

#print(solution(routes))