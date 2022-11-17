student_name = str(input("Enter User Name:")).capitalize()
tamil_mark = float(input("Enter Tamil Mark:")) 
english_mark = float(input("Enter English Mark:"))
maths_mark = float(input("Enter Maths Mark:"))
physics_mark = float(input("Enter Physics Mark:"))
chemistry_mark = float(input("Enter Chemistry Mark:"))
computer_mark = float(input("Enter Computer Mark:"))


def generate_result(mark):
    result = "Fail"
    if (mark >= 0 and mark <= 100):
        if (mark >= 35):
            result = "Pass"
    else:
        print("Invalid Input Mark should be Positive and Less 100")
    return result


tamil_result = generate_result(tamil_mark)
english_result = generate_result(english_mark)
maths_result = generate_result(maths_mark)
physics_result = generate_result(physics_mark)
chemistry_result = generate_result(chemistry_mark)
computer_result = generate_result(computer_mark)
overall_result = ""
grand_total = int(tamil_mark+english_mark+maths_mark + \
    physics_mark+chemistry_mark+computer_mark)

if (tamil_result == "Pass" and english_result == "Pass" and maths_result == "Pass"
        and physics_result == "Pass" and chemistry_result == "Pass" and computer_result == "Pass"):
    overall_result = "Pass"
else:
    overall_result = "Fail"


# if (tamil_result == "Fail" or english_result == "Fail" or maths_result == "Fail"
#         or physics_result == "Fail" or chemistry_result == "Fail" or computer_result == "Fail"):
#     overall_result = "Fail"
# else:
#     overall_result = "Pass"

print("===========================")
print("Student Name | ", student_name)
print("---------------------------")
print("Subject  |  Mark |  Result")
print("---------------------------")
print("Tamil    | " + str(tamil_mark)+"  |  "+tamil_result)
print("English  | " + str(english_mark)+"  |  "+english_result)
print("Maths    | " + str(maths_mark)+"  |  "+maths_result)
print("Physics  | " + str(physics_mark)+"  |  "+physics_result)
print("Chemistry| " + str(chemistry_mark)+"  |  "+chemistry_result)
print("Computer | " + str(computer_mark)+"  |  "+computer_result)
print("---------------------------")
print("Total    | "+str(grand_total)+"  |  "+overall_result)
print("===========================")
