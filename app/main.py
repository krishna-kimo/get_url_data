import base64
import json
import os

from google.cloud import pubsub_v1


# Instantiates a Pub/Sub client
publisher = pubsub_v1.PublisherClient()
PROJECT_ID = "kimo-kube"
GET_URL_DATA_TOPIC_ID="get-url-data"
PROCESS_DATA_TOPIC_ID="process_data"


# Publishes a message to a Cloud Pub/Sub topic.
def publish(request):
    request_json = request.get_json(silent=True)

    topic_name = TOPIC_ID
    message = request_json.get("message")

    if not topic_name or not message:
        return ('Missing "topic" and/or "message" parameter.', 400)

    print(f'Publishing message to topic {topic_name}')

    # References an existing topic
    topic_path = publisher.topic_path(PROJECT_ID, topic_name)

    message_json = json.dumps({
        'data': {'message': message},
    })
    message_bytes = message_json.encode('utf-8')

    # Publishes a message
    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()  # Verify the publish succeeded
        return 'Message published.'
    except Exception as e:
        print(e)
        return (e, 500)


# Triggered from a message on a Cloud Pub/Sub topic.
def subscribe(event, context):
    # Print out the data from Pub/Sub, to prove that it worked
    ## Fetches the url from the pub/sub and process it and send push it to the Pub/Sub again
    print(base64.b64decode(event['data']))