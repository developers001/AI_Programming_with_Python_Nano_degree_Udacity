def function(input1, input2):
    #case_1: Where both of inputs are numericals
    if (isinstance(input1, (int, float)) and isinstance(input2, (int, float))):#checking the data format
        if input2 !=0:
            print((input1 + input2),(input1 - input2),(input1 * input2),str(int((input1 / input2) * 100))+"%")
        else:
            print((input1 + input2),(input1 - input2),(input1 * input2), "Zero Division Error")
    #case_2: Where both of inputs are not numericals
    elif not isinstance(input1, (int, float)) and not isinstance(input2, (int, float)):#checking the data format
        input_string = str(input1) + str(input2)
        print(input_string,", Other operations are not applicable")
    #case_3: Where one of the input is not numericals
    else:
        num_text = str(input1) + str(input2)
        multi = input1 * input2
        print(num_text, multi)


#Expected Outputs terminal
function(2,3)
function("Hi"," Raju")
function(2,"Raju")