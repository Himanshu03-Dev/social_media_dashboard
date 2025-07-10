import requests
from requests_oauthlib import OAuth1
from django.conf import settings

# ✅ Fetch Tweets using Bearer Token
def fetch_twitter_posts():
    try:
        headers = {"Authorization": settings.TWITTER_BEARER}
        user_id = "1939618333571284992"  # Your actual Twitter User ID

        response = requests.get(
            f"https://api.twitter.com/2/users/{user_id}/tweets",
            headers=headers
        )

        if response.status_code == 200:
            return response.json().get("data", [])

        print("Twitter API Error:", response.status_code, response.text)
    except Exception as e:
        print("Twitter Fetch Exception:", str(e))
    return []


# ✅ Post Tweet using OAuth 1.0a
def post_to_twitter(content):
    try:
        url = "https://api.twitter.com/2/tweets"

        auth = OAuth1(
            settings.TWITTER_CONSUMER_KEY,
            settings.TWITTER_CONSUMER_SECRET,
            settings.TWITTER_ACCESS_TOKEN,
            settings.TWITTER_ACCESS_TOKEN_SECRET
        )

        payload = {"text": content}
        response = requests.post(url, json=payload, auth=auth)

        if response.status_code in [200, 201]:
            print("Tweet posted successfully.")
            return True

        print("Twitter Post Error:", response.status_code, response.text)
    except Exception as e:
        print("Twitter Post Exception:", str(e))
    return False



# ✅ Fetch Facebook Page Posts
def fetch_facebook_posts():
    try:
        access_token = settings.FB_ACCESS_TOKEN
        page_id = settings.FB_PAGE_ID

        url = f"https://graph.facebook.com/v19.0/{page_id}/posts?access_token={access_token}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get("data", [])

        print("Facebook API Error:", response.status_code, response.text)
    except Exception as e:
        print("Facebook Fetch Exception:", str(e))
    return []


# ✅ Post to Facebook Page
def post_to_facebook(content):
    try:
        access_token = settings.FB_ACCESS_TOKEN
        page_id = settings.FB_PAGE_ID

        url = f"https://graph.facebook.com/v19.0/{page_id}/feed"
        payload = {"message": content, "access_token": access_token}

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print("Facebook Post Successful.")
            return True

        print("Facebook Post Error:", response.status_code, response.text)
    except Exception as e:
        print("Facebook Post Exception:", str(e))
    return False
