#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

LINEBOT_API_EVENT ='https://trialbot-api.line.me/v1/events'

LINE_HEADERS = {
    'Content-type': 'application/json; charset=UTF-8',
    'X-Line-ChannelID':'xxxxxxxxx',
    'X-Line-ChannelSecret':'xxxxxxxxxxxxxxxxxxxxxxxx',
    'X-Line-Trusted-User-With-ACL':'xxxxxxxxxxxxxxxxxxxxxxxxx'
}

def handler(event, context):
    try:
        logger.info(event)
        msg = event['result'][0]
        text = msg['content']['text']
        from_id = msg['content']['from']

        content = {
            'contentType':1,
            'toType':1,
            'text':text
        }

        send_msg = {
            'to':[from_id],
            'toChannel':1383378250,
            'eventType':'138311608800106203',
            'content':content
        }

        post_response = requests.post(LINEBOT_API_EVENT,headers=LINE_HEADERS,data=json.dumps(send_msg))
        logger.info(post_response)
    except Exception as e:
        logger.info(e)
        raise e





