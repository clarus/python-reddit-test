import praw
import urllib.request

r = praw.Reddit(user_agent="clarus_tester")
submissions = r.get_subreddit("aww").get_hot(limit=5)
for submission in submissions:
    print("Downloading", submission.title)
    picture = urllib.request.urlopen(submission.url).read()
    output = open("pictures/" + str(submission.score) + ".jpg", "wb")
    output.write(picture)
    output.close()
