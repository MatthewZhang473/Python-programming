def find_string(s,head,tail):
    # head is the index of the first element, tail is the index of the final element +1

    # ending condition of the recursion
    count_bracket = False
    for i in range(head,tail):
        if s[i] == "[" or s[i] == "]":
            count_bracket = True
            break
    if count_bracket == False:
        return s[head:tail]

    else:
        # if there is bracket, solve the problem by recursion
        # record the index of the number of multiple before the bracket
        multiple_pointer_head = head
        multiple_pointer_tail = head
        # sections records all sections of the string
        sections = []
        # is_multiple record if the current pointer is in the multiple part or inside the bracket
        is_multiple = True
        # count the number of brackets,counter = 0 means a bracket is closed
        counter = 0

        for j in range(head,tail):
            if s[j] == "[":
                # counter increases if there is a "["
                counter += 1
                if is_multiple == True: # if it is the first time we encounter a bracket
                    multiple_pointer_tail = j # record the index of the last digit of the multiple +1
                is_multiple = False # from now j is inside the bracket
            
            if s[j] == "]":
                # counter -1 when we meet a "]"
                counter -= 1
    
            if counter == 0 and is_multiple == False:
                # when a bracket closes
                is_multiple = True #reset the is_multiple
                multiple = int(s[multiple_pointer_head:multiple_pointer_tail]) # find the number of multiple infront of the bracket
                sections.append(multiple * find_string(s,multiple_pointer_tail+1,j)) # add this sub-section
                multiple_pointer_head = j+1 # update the position of pointer
        
        result = ""
        for section in sections:
            result += section
        return result


the_string = "3[2[abd]3[c]]2[f]"
print(find_string(the_string, 0,len(the_string)))

