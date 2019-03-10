+#!/bin/sh

SCRIPT_PATH=$(dirname ${0})
RET=$(ps alx | grep mhw_bot | grep -v grep | grep -v activate | wc -l)
echo ${RET}

if [ ${RET} -eq 0 ]; then
    echo "activate bot"
    cd "${SCRIPT_PATH}"
    python3 ./mhw_bot.py > /dev/null 2>&1 &
else
    echo "running"
fi