

def getting_info(name_file,distance_file):

    '''reading name file into list of string'''

    with open(f'{name_file}','r') as readfile:
        cities_list = readfile.read().splitlines()

    '''reading distance file into list of float'''

    with open(f'{distance_file}') as readfile:
        distance_str = readfile.read()
        distance_str = distance_str.split()
    distance_flt = []
    for string in distance_str:
        string = float(string)
        distance_flt.append(string)

    '''creating dictionary (city i,city j):distance from i to j'''

    names_distance = {}
    flag_dist = 0
    for name1 in cities_list:
        for name2 in cities_list:
            names_distance[name1,name2] = distance_flt[flag_dist]
            flag_dist += 1

    return cities_list,names_distance

import random

''' calculate the distance of a route'''

def getting_distance(name_list,dict):
    distance = 0
    for i in range(len(name_list)):
        if i == (len(name_list)-1):
            distance += dict[name_list[i],name_list[0]]
        else:
            distance += dict[name_list[i],name_list[i+1]]
    return round(distance,1)

tsp = []
def tsp_greedy(name_file, distance_file):
    list_of_names ,names_distance = getting_info(name_file,distance_file)
    for name in list_of_names:
        candidate_route = []
        candidate_route.append(name)
        for i in range(len(list_of_names)):
            if len(candidate_route) == len(list_of_names):
                global tsp
                tsp_distance = getting_distance(tsp, names_distance)
                candidate_dist = getting_distance(candidate_route, names_distance)
                if tsp_distance > candidate_dist or tsp_distance == 0:
                    tsp = candidate_route
                    tsp_distance = candidate_dist
                    
                
            else:
                distance_frm_name = 0
                for key in names_distance.keys():
                    if candidate_route[-1] == key[0] and key[-1] not in candidate_route:
                        if names_distance[key] < distance_frm_name or distance_frm_name == 0:
                            distance_frm_name = names_distance[key]
                            next_closest_city = key[1]
                candidate_route.append(next_closest_city)

    print(f'{tsp}, this is the route and {tsp_distance} is the added distance of all cities. ')
                    
            
            
            
tsp_greedy('thirty_cities_names.txt', 'thirty_cities_dist.txt')
                
                
        
        
        
        