import base64
import json
import os

from google.cloud import pubsub_v1


class KimoPubSub():
    def __init__(self, url_rec_sub, data_pub_topic):
        self.url_rec_sub = url_rec_sub
        self.data_pub_topic = data_pub_topic


    