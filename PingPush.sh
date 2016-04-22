#!/bin/bash

API="$1"
TTL="$2"
MSG="$3"

curl -u $API: https://api.pushbullet.com/v2/pushes -d \
	type=note -d title="$TTL" -d body="$MSG"

