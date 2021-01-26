                                '''Lectures by Ravula Govardhan'''
                        '''-----------------------------------------------'''
                        '''LIKE SHARE COMMENT (SUBCRIBE & CLICK BELL)'''

movie = ["movie1", "movie2", ["movie3", ["movie4", "movie5","movie6", "movie7"]]]

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
		
        
'''Create a function'''
'''----------------------------------------------------------'''

'''def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movie)'''


movies1 = ['movies1', 'movies2', ['movies3',['movies4', 'movies5', 'movies6', ['movies7','movies8', 'movies9']]]]

'''def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            
print_lol(movies1)'''


names = ['a', 'b', ['c', ['d', 'e', 'f', ['g', 'h', 'i', ['j', 'k']]]]]

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            
print_lol(names)

