from time import sleep
from jupyter_helpers.following_tail import FollowingTail

display_no_more_than_five = FollowingTail(n=5)
display_no_more_than_five.activate()

for i range(20):
	display_no_more_than_five(i)
	sleep(0.2)


	
	
	