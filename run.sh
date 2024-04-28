#!/bin/bash

# RUN get_data.sh file first....
bash ./log_reader.sh

# Filter data from the result.txt

# 1. Read the data from result.txt....
# 2. This logic is based on how you want to grep data from where...
# 3. It will do text based search only for "callName|session"
# 4. Store the data in result.txt...........................................

#	1		2		3				4
cat  custom_log.txt |cut -d "," -f2-11|grep -i -E "callName|session" > result.txt

# 5. Modify result.txt by removing special character.........................
 sed -i -e "s/=/:/g; s/\[\]//g; s/(/,/g;s/)/'null'/g" result.txt
