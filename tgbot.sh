TGBOT=6003194653:AAF5PviH8BBqMRgaxhKfH-coLc-OwTPNIME
CHAT_ID=222536676

curl -s -o /dev/null -X POST https://api.telegram.org/bot$TGBOT/sendMessage -d chat_id=$CHAT_ID -d text="$(date +'%Y%b%d %H:%M:%S') : github update"

echo "done"
exit