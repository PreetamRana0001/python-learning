# write  a program to find out whether a student is passed or fails , if it requires total. 40% 
# and at least 33% in each subject to pass. assume 3 sunject and take marks as an input from the user

sub1 = float(input("enter  marks of first subject: "))
sub2 = float(input("enter  marks of second subject: "))
sub3 = float(input("enter  marks of third subject: "))   

total = sub1 + sub2 +sub3
percentage = (total/300) * 100
if(percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("congratulation you have passed the exam", percentage)

else:
    print(f"{percentage}fail")