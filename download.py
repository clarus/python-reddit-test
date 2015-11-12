import praw
import csv

r = praw.Reddit(user_agent="clarus_tester")
submissions = r.get_subreddit("aww").get_new(limit=1000)
with open("images.csv", "w", newline="") as output:
    writer = csv.writer(output)
    for submission in submissions:
        print(submission.score, submission.title)
        writer.writerow([submission.score, submission.title])
