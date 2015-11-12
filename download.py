import praw

r = praw.Reddit(user_agent="clarus_tester")
submissions = r.get_subreddit("aww").get_hot(limit=5)
for x in submissions:
    print(x.score, x.url)
