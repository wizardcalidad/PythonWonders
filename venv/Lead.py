LeadingTeam_str = input('enter the number of points team one is leading with: ')
LeadingTeam = int(LeadingTeam_str)
LeadingTeam = LeadingTeam - 3
hasball = input('press y/n if leading team has ball or not')
if hasball=='y':
    LeadingTeam = LeadingTeam + 0.5
elif hasball =='n':
    LeadingTeam = LeadingTeam - 0.5
LeadingTeam = LeadingTeam**2

time = int(input('how many seconds left till end of game'))
if LeadingTeam > time:
    print("The lead is safe")
else:
    print("The lead is not safe")


