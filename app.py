import logging
import os
from typing import List
from slack_bolt import App
from slack_bolt.error import BoltError
import time

import requests

# Create the Slack instance with the bot token from environment variables
app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = app.client

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def send_hackernews_alerts(keywords: List[str], user_ids: List[str],
                           num_top_stories: int) -> None:

  logger.info("🏃‍♂️ Fetching to stories")

  # fetch top stories from Hacker News
  top_story_ids = requests.get(
      "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty",
      time.sleep(.1)).json()[:num_top_stories]

  logger.info("🤔 Getting story details")

  # get details
  story_data = [
      requests.get(
          f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json(
          ) for story_id in top_story_ids
  ]

  # filter stories
  filtered_stories = [
      s for s in story_data if s.get('type') == 'story' and s.get('url')
  ]

  matches = []

  # find matches
  for story in filtered_stories:
    for k in keywords:
      if k.lower() in story.get('title').lower() and k.lower() in story.get(
          'url').lower():
        matches.append(story)

  alert_str = "New stories matching your keywords:"

  for match in matches:
    title = match['title'].replace("https://", "")
    alert_str += f"\n- <{match['url']}|{title}>"

  logger.info("📨 Sending alert")

  # alert users
  for user_id in user_ids:
    try:
      channel_id = client.conversations_open(users=[user_id])['channel']['id']
    except BoltError as e:
      logger.info(f"❌ Error opening channel with user: {user_id}")
      raise e

    client.chat_postMessage(channel=channel_id, text=alert_str, mrkdwn=True)

    logger.info(f"Sent alert to user: {user_id}")


if __name__ == "__main__":
  KEYWORDS = ["h"]
  ALERT_UIDS = ["U05UJUG31PU"]
  # max 500
  NUM_TOP_STORIES = 25

  send_hackernews_alerts(KEYWORDS, ALERT_UIDS, NUM_TOP_STORIES)
