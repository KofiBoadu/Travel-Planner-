def trip_planner(destination,numb_stays,accomodation_type,numb_people):
    
# using 4 parameters to check for the travelers destination,number of stays,room type,and the number of people
# traveling
    
    
    destination1=["Ghana","Congo","Kenya"]
    accomodation_type1=[3,4,5]
    
    
# since we are checking for only 3 destinations, i created a list to specify these locations and loop through

# since we have only 3-5 star hotels i decided to specify by creating a list for 3-5 star hotels
   
        
        
    if (destination==destination1[0]) and (numb_stays <=4) and (numb_people >=4) and (accomodation_type in accomodation_type1):
        
        return "Cost per person== $2000"
    
    
#  over here i jsut checked to see if it meets all the conditions requested using ghana as the first destination 

    if(destination==destination1[0]) and (numb_stays >=4) and (numb_people >=4) and (accomodation_type in accomodation_type1):
        
        return "cost per person== $3,000"
    

# checking to see if the number of stays are more than 4 days ?

        
    if destination==destination1[1] and (numb_stays <=4) and (numb_people >=4) and (accomodation_type in accomodation_type1):
            
            return "cost per person ==$5,000"
        
# over since im checking for other locations i specified the index to check for only congo since kenya has a 
# diferent condition

    if destination==destination1[2] and (numb_stays <=4) and (numb_people >=4) and (accomodation_type in accomodation_type1):
            
            return "cost per person==$10,000"
        
    
# I checked to see if the destination is kenya and meets all the other conditions specified for Ghana?
        
    
       
            
    else:
            
            return "Please talk to our customer service at 866-783-5188!"
        
        
# if all conditions dont meet ? it should tell the customer to call us 

        
        
destination= input("where do you want to travel to ?: ").capitalize()

numb_stays= int(input("How many days do you want to stay ?: "))

accomodation_type= int(input("what type of accommodation do you want: "))

numb_people= int(input("How many people are you traveling with?: "))


print(trip_planner(destination,numb_stays,accomodation_type,numb_people))