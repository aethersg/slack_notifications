# slack_notifications
Python language to use slack notifications

Very simple slack client by using slack api webhook.

## How to install

To install slack-notifications, simply:

<pre>
$ sudo pip install slack_notification
</pre>

or from source:

<pre>
$ sudo python setup.py install
</pre>

## Getting started

Get a token of slack webhook on [slack page](https://my.slack.com/services/new/incoming-webhook/).

Instantiate:
<pre>
> import slack_notification
> slack = slackweb.Slack(url="https://hooks.slack.com/services/XXXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX")
</pre>

In case that you want to send a simple message:

<pre>
> slack.notify(text="Don't even trip dawg")
</pre>

In case that you want to send a custom message:

<pre>
> slack.notify(text="get schwifty!!", channel="#showmewhatyougot", username="rick")
</pre>

More detail description of message formatting, refer according pages:

- [Message Formatting](https://api.slack.com/docs/formatting)
- [Attachments](https://api.slack.com/docs/attachments)
