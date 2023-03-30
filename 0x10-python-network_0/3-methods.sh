#!/bin/bash
#display allowed methods of header
curl -sI "$1" | grep "Allow:" | cut -f 2- -d " "
