# IF helps your program make decisions based on conditions,
# ELIF lets you check for more conditions if the first one isn't true,
# ELSE gives an alternative if the condition isn’t met
# The order of the IF and ELIF is very important, because once you agree to enter an IF you will no longer enter the ELIF.
# ELIF is not used as much as the IF and ELSE.

hour = 14

# Check the time of the day
if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good evening")
