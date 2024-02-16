import sys
import time

import Utils
from InstagramClient import InstagramClient
from RedditPost import RedditPost


def main(config_path):
    #   get config file
    configs = Utils.read_config_file(config_path)

    reddit_username = configs['Reddit']['username']
    reddit_password = configs['Reddit']['password']
    reddit_client_id = configs['Reddit']['client_id']
    reddit_client_secret = configs['Reddit']['client_secret']
    sub_reddit = configs['Reddit']['subreddit']

    instagram_username = configs['Instagram']['username']
    instagram_password = configs['Instagram']['password']

    temp_photo_path = configs['MISC.']['temp_photo_path']

    current_try = 0
    MAX_RETRIES = 5

    while current_try < MAX_RETRIES:
        try:
            #   get reddit post
            reddit_post = RedditPost(reddit_username, reddit_password, reddit_client_id, reddit_client_secret)
            df = reddit_post.posts_as_dataframe(sub_reddit, 5)
            post = df.iloc[current_try]
            title = post['Title']
            author = post['Author']
            url = post['URL']
            permalink = post['Permalink']
            comment = f"{title}.\n\nImagem postada por u/{author}. Obrigado! (link: https://reddit.com{permalink})"

            #   get photo
            Utils.url_to_image(url, temp_photo_path)

            #   post to instagram
            instagram_client = InstagramClient(instagram_username, instagram_password)
            instagram_client.post_image(temp_photo_path, comment)

            #   delete temp photo
            Utils.delete_temp_file(temp_photo_path)

            print("Posted!")
            break

        except:
            current_try = current_try + 1
            print("An error occurred, sleeping for 15min")
            time.sleep(900)


if __name__ == "__main__":
    main(sys.argv[1])
