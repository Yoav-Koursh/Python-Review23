
import speech_recognition
import pyttsx3
def create_youtube_video( hashtag):
	hashtag = hashtag[:4]
	title= speach_rec("Title")
	title=title[11:]
	discription= speach_rec("discription")
	discription=discription[11:]
	video= { "title":title, "description": discription, "likes":0, "dislikes":0, "comments":{}, "hashtag":hashtag}
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
def speach_rec(object):
	recognizer= speech_recognition.Recognizer()
	print("please state "+ object)
	while True:
		try:
			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=1)
				audio= recognizer.listen(mic)
				text= recognizer.recognize_google(audio)
				text= text.lower()
				return (f"recognized {text}")
		except speech_recognition.UnknownValueError():
			continue
vid1= create_youtube_video( ["sick", "cool", "a", "b", "c", "d"])
print (vid1)
vid1= like(vid1)
vid1= add_comment(vid1, "user1", "cool vid!")
vid2= create_youtube_video( ["sick", "cool", "h", "g", "f", "e"])
print (similarity_to_video(vid1,vid2))
