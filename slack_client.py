from slacker import Slacker


def send_message(message, token):
    api_client = Slacker(token)
    _send_slack_message(message, api_client)


def _send_slack_message(message, slack_client):
    im_response = slack_client.im.open("#test-sourcing")
    im_channel_id = im_response.body["channel"]["id"]
    print(message)
    slack_client.chat.post_message(im_channel_id, message,
                                   as_user=True, parse="none")
    slack_client.im.close(im_channel_id)
