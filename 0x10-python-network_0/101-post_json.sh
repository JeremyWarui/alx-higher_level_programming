#!/bin/bash
#post json file in url
curl -sH 'Content-Type: appliction/json' -d @"$2" -X POST "$1"
