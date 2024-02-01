import json
from datetime import datetime
from json import JSONEncoder

import facebook_scraper as fs
from fastapi import FastAPI
from pydantic import BaseModel

MY_CREDENTIALS = ()
app = FastAPI()


class ParsePostRequest(BaseModel):
    post_url: str
    description: str = None


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return JSONEncoder.default(self, o)


@app.get("/posts")
def read_items():
    group = fs.get_group_info("ezduni")
    group_id = group.get("id")

    #   gen = fs.get_posts(
    #       account="max.thraex",
    #       group=group_id,
    #       pages=3, timeout=60_000, credentials=my_credentials,
    #       options={"comments": False, "reactors": False, "allow_extra_requests": False, "progress": False}
    #   )
    gen = fs.get_posts(
        post_urls=iter([
            "https://www.facebook.com/photo/?fbid=892959649500743&set=a.634411518688892",
            "https://www.facebook.com/groups/ezduni/permalink/2433004186886440/?mibextid=oMANbw",
            "https://www.facebook.com/onoffapp/posts/pfbid0vkbGbhjPyHYrSTJcxgeM3BvVpRfJLhG4T2w9eiY6NHZ814vTgUZt7XNWK6oJexzrl",
            "https://www.facebook.com/groups/zaliponclub/permalink/7126629687450172/"
        ]),
        timeout=60_000,
        credentials=MY_CREDENTIALS,
        options={"comments": False, "reactors": False, "allow_extra_requests": False, "progress": False}
    )
    posts = list(gen)
    counter = len(posts)
    while len(posts) > 0:
        post = posts.pop()
        print("RAW DATA: ", json.dumps(post, cls=CustomEncoder))
        if post is None:
            print("post is None")
        else:
            print("POST: ", post["post_id"])
            comments = post['comments_full']
            for comment in comments:
                print(comment)

    return {"group-id": group_id, "group-name": group.get("name"), "post-counter": counter}


# Parse FB post endpoint
@app.post("/parse-post")
def parse_post(request: ParsePostRequest):
    gen = fs.get_posts(
        post_urls=iter([
            request.post_url
        ]),
        timeout=60_000,
        # credentials=MY_CREDENTIALS,
        options={"comments": False, "reactors": False, "allow_extra_requests": False, "progress": False}
    )
    posts = list(gen)
    if len(posts) == 0:
        return {}
    post = posts.pop()
    return post
