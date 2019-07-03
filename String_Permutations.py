def matchFunction (s, b):
    match = 0
    counter = 0
    for i in b:
        
        count = 0

        #For loop looks for at least 1 match
        for a in s:
            if a == i:
                count += 1
                
        #If 1 match then add it to a match.      
        if count >= 1:
            match += 1

        #If no matches then 0 out matches 
        else:
            match = 0
            
        counter += 1
        location=0
        #If there are at least 4 matches then find the location of the 4 matches
        if match >= len(s):
            location = counter - len(s)
            

            print("current match is, ",match)
            print(location)
            location = 0
            
            
            
        
            
            
        
        
s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"
matchFunction(s,b)


        
