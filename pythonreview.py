def create_youtube_video( title, description):
	video= { "title":title, "description": description, "likes":0, "dislikes":0, "comments":{}}
	return video
def like(dictinary):
	try:
		dictinary["likes"]+=1
	except:
		pass
	return dictinary
def dislike(dictinary):
	try:
		dictinary["dislikes"]+=1
	except:
		pass
	return dictinary
def add_comment( vid, username, comment):
	vid["comments"][username]= comment
	return vid
vid= create_youtube_video("hello","checking")
vid= like(vid)
vid= add_comment(vid, "user1", "cool vid!")
print (vid)