#!/bin/bash
# Send a GET request to a given URL and displays the body of the response.
curl -sX GET -H "X-School-User-Id: 98" "$1"
