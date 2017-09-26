name = ['lol12','lolita','genji','mccree','widow']
newname = input(['soldier','lolita','ash','sledge','twitch'])
new=[]
for x in newname:
    if x in new:
        print('the name ' , x , ' exist already, find another')
    else:
        print('the name ' , x ,'is avaible, you can use the name')
