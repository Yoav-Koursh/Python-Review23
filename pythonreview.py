def create_youtube_video( title, description, hashtag):
	hashtag = hashtag[:4]
	video= { "title":title, "description": description, "likes":0, "dislikes":0, "comments":{}, "hashtag":hashtag}
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
def similarity_to_video(vid1, vid2):
	similarity_count=0
	for i in range (4):
		for x in range (4):
			if vid1["hashtag"][i]== vid2["hashtag"][x]:
				similarity_count+=1
				break
	similarity_precent=similarity_count*20
	return similarity_precent
vid1= create_youtube_video("hello","checking", ["sick", "cool", "a", "b", "c", "d"])
vid1= like(vid1)
vid1= add_comment(vid1, "user1", "cool vid!")
vid2= create_youtube_video("hello","checking", ["sick", "cool", "h", "g", "f", "e"])
print (similarity_to_video(vid1,vid2))
