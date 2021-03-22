import requests
import logging
import json
from post import Post

logging.basicConfig(level=logging.NOTSET)


def call_api(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_age(name) -> str:
    params = {"name": name}
    json = call_api("https://api.agify.io", params)
    return json["age"]


def get_gender(name) -> str:
    params = {"name": name}
    json = call_api("https://api.genderize.io", params)
    return json["gender"]


def get_posts() -> list:
    json_posts = call_api("https://api.npoint.io/5abcca6f4e39b4955965")
    # print(json.dumps(json_posts, indent=4))
    posts = []
    for json_post in json_posts:
        post = Post(
            json_post["id"],
            json_post["title"],
            json_post["subtitle"],
            json_post["body"]
        )
        posts.append(post)
    return posts


if __name__ == "__main__":
    name = "michael"
    age = get_age(name)
    gender = get_gender(name)
    print(name, age, gender)

    posts = get_posts()
    print(posts)
