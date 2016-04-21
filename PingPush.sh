#!/bin/bash

API="$1"
MSG="$2"

curl -u $API: https://api.pushbullet.com/v2/pushes -d \
	type=note -d title="Mailbox Alert" -d body="$MSG"

