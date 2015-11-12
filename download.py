import praw
import os

r = praw.Reddit(user_agent="clarus_tester")
submissions = r.get_subreddit("aww").get_hot(limit=20)
for submission in submissions:
    _, extension = os.path.splitext(submission.url)
    print(submission.score, extension)
