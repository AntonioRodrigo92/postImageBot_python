import pandas as pd
import praw


class RedditPost:
    reddit_user = None

    def __init__(self, username, password, client_id, client_secret):
        user_agent = "praw_scraper_1.0"
        self.reddit_user = praw.Reddit(
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def posts_as_dataframe(self, subreddit_name, post_limit):
        subreddit = self.reddit_user.subreddit(subreddit_name)
        df = pd.DataFrame()
        titles = []
        authors = []
        urls = []
        permalinks = []

        for submission in subreddit.top(time_filter="day", limit=post_limit):
            titles.append(submission.title)
            authors.append(submission.author)
            urls.append(submission.url)
            permalinks.append(submission.permalink)

        df['Title'] = titles
        df['Author'] = authors
        df['URL'] = urls
        df['Permalink'] = permalinks

        return df
