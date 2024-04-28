#!/bin/bash

# It will read the log and do text based search and store
# the result in custom_log.txt.............................
cat log|grep -i FileRecordingRequestParams >> custom_log.txt
