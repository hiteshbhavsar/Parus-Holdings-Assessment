import os
import sys
import json
import operator

# This is a class to store the name of the commodity and the price
class _Items: 

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return str(self.name)+":"+str(self.price)

    def __repr__(self):
        return str((self.name, self.price))

def readJson(file_name):
    '''
    This function is used to read the file with name file_name from the directory
    and store the values of target and the dishes available in dictionary format
    '''
    try:
        # Opening  file to read from
        file = open(file_name)
        # returns JSON object as a dictionary
        
        data = json.load(file)
        # Iterating through the json
        # list
        _target=float(data['Target Price']) # fetching the target Price value from the file
	
        list_of_items=[] # its used to store the list of all the item to choose

        for i in data['items']:
            item=_Items(i['Name'],float(i['Price']))
            list_of_items.append(item)
        file.close()
    except (ValueError,KeyError,UnboundLocalError) as verr:
        print("Please check the format of input file")
        return
    except FileNotFoundError as ferr:
        print("The input file name passed in the parameter was not found in the current directory")
        return
    
    return (_target,list_of_items)

    
	
result=[]

def combinations(list_of_items,target):
        # This function is to sort the list of all the dishes and give out the combination of the dishes
                
	combination=[]
	list_of_items=sorted(list_of_items, key=lambda x: x.price)
	find_combinations_of_Dishes(combination,list_of_items,target,0,0,target)
	return result

def find_combinations_of_Dishes(combination,list_of_items,target,index,sum_of_price,final_target):
    '''
    This is a helper function used to check all possible combination of dishes and return the list
    of all possible combination of dishes
    '''
    if(sum_of_price==final_target or target==0):
        result.append(combination.copy())
        return
    if(target<0 or index==len(list_of_items)):
        return
    for a in range(index,len(list_of_items)):
        sum_of_price+=list_of_items[a].price
        combination.append(list_of_items[a])
        find_combinations_of_Dishes(combination,list_of_items,target-list_of_items[a].price,a,sum_of_price,final_target)
        sum_of_price-=list_of_items[a].price
        combination.pop()
    return


if __name__ == "__main__":
    
    file_name=''
    if len(sys.argv)>1:
        file_name=sys.argv[1]
    else:
        file_name='input.json'
    print('Input File Name : '+str(file_name))
    values=()
    values=readJson(file_name)
    target=0
    list_of_items=[]
    if(values!=None):
        target,list_of_items=readJson(file_name)
    if(target==0 or list_of_items==0):
        print("The input file is empty please add the data in json format")
        pass
    print("Target value : "+str(target))
    print("Items/Dishes : ")
    print(list_of_items)
    print()
    final_result=combinations(list_of_items,target)
    if(len(final_result)==0):
    	print("There is no combination of dishes that is equal to the target price")
    	pass
    elif(len(list_of_items)==0):
        print("There are no dishes in input json file. Please check the input file")
        pass
    else:
        print("Total number of combinations available : "+str(len(final_result)))
        print("The available combinations of dishes that sums up to target are as follows")
        
        for x in final_result:
            print(x)
            '''
            dictionary={}
            s= ""
            for item in x:
                if(item.name in dictionary):
                    dictionary[item.name]+=1
                else:
                    dictionary[item.name]=1
            
            for k,v in dictionary.items():
                s+=str(v)+" number of "+str(k)+"\n"
            '''
            
        
            
    pass



#print(list_of_items)





    
        
    
    


