fav_movies = ["movie1","movie2", "movie3","movie4","movie5"]

'''print(fav_movies[0])
print(fav_movies[1])
print(fav_movies[2])'''


'''for each_item in fav_movies:
    print(each_item)'''
    
'''count = 0
while count<len(fav_movies):
    print(fav_movies[count])
    count = count+1'''
    
movie = ["movie1", "movie2", ["movie3", ["movie4", "movie5","movie6", "movie7"]]]

'''print(movie[0])
print(movie[1])
print(movie[2])'''

'''print(movie[2][1][0])
print(movie[2][1][3])'''

'''for each_item in movie:
    print(each_item)'''

'''if..else..pattern

if some_condition_holds:
    the "true" suite
else:
    the "false" suite'''
    
'''names = ['mayuri', 'kartheek']
isinstance(names, list)

num_names = len(names)
isinstance(num_names, list)'''

movie = ["movie1", "movie2", ["movie3", ["movie4", "movie5","movie6", "movie7"]]]

'''for each_item in movie:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)'''
        
'''for each_item in movie:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deper_item in nested_item:
                    print(deper_item)
            else:
                print(nested_item)
    else:
        print(each_item)'''
        
'''for each_item in movie:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deper_item in nested_item:
                    if isinstance(deper_item, list):
                        for depest_item in deper_item:
                            print(depest_item)
                    else:
                        print(deper_item)
            else:
                print(nested_item)
    else:
        print(each_item)'''
        

    
    
    
    
    
    
    
    
    

