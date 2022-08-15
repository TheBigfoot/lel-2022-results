#!/bin/bash

# get token and cookie from a valid browser session (Chrome inspect)
COOKIE='...'
TOKEN='...'

while read -r line
do 
  for i in $(seq 1 100)
  do
    echo "Rider result for ${line}${i}"
    result=$(curl -s "https://londonedinburghlondon.com/ridertracking?daisnotspam=1&token=${TOKEN}&rider_no=${line}${i}&ajax=1" \
      -H 'Accept: application/json, */*; q=0.01' \
      -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
      -H 'Connection: keep-alive' \
      -H "${COOKIE}" \
      -H 'Referer: https://londonedinburghlondon.com/ridertracking' \
      -H 'Sec-Fetch-Dest: empty' \
      -H 'Sec-Fetch-Mode: cors' \
      -H 'Sec-Fetch-Site: same-origin' \
      -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36' \
      -H 'X-Requested-With: XMLHttpRequest' \
      -H 'sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"' \
      -H 'sec-ch-ua-mobile: ?0' \
      -H 'sec-ch-ua-platform: "macOS"' \
      --compressed)
    if [[ $result =~ 'has not yet registered to ride' ]] || [[ $result =~ 'Rider not found' ]]; then
      echo "Invalid result, skipping"
    else
      echo "Valid result, saving into ${line}${i}.txt"
      echo $result > results/${line}${i}.txt
    fi
  done
done < letters.txt
