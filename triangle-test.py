
def is_triangle(i, j, k):
    if((i > j+k) or (j > i+k) or (k > i+j)):
        print "No"
    else:
        print "Yes"

iTxt = raw_input('What is the first triangle length?\n')
jTxt = raw_input('What is the second triangle length?\n')
kTxt = raw_input('What is the third triangle length?\n')

is_triangle(int(iTxt), int(jTxt), int(kTxt))
    
