score = input('Enter Score:')
try:
    scr = float(score)
except:
    print ('Input Error')
    quit()
if scr >=1:
    print ('Incorrect Score Entered')
elif scr <0:
    print ('Incorrect Score Entered')
elif scr >=0.9:
    print ('Grade A')
elif scr >=0.8:
    print ('Grade B')
elif scr >= 0.7:
    print ('Grade C')
elif scr >=0.6:
    print ('Grade D')
else: #scr <0.6:
    print ('Grade F')
