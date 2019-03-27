#!/bin/bash
# based on GtkGrab by @EvanDotPro https://github.com/EvanDotPro/GtkGrab
function rename_file()
{
    NEWFILE=$(echo $1 | md5sum | cut -c-25)'.png'
}
REMOTE=mindey@wiki.mindey.com:/home/mindey/hosts/wiki/shared/shots/
DOMAIN=https://wiki.mindey.com/shared/shots/
LOCALPATH=/home/mindey/Pictures/screens/
xfce4-screenshooter -r --save=$LOCALPATH
LOCALFILE=$(ls -tr $LOCALPATH | tail -n 1)
rename_file $LOCALFILE
I=0
LIMIT=10
while [ "$I" -lt "$LIMIT" -a -f "$LOCALPATH$NEWFILE" ]
do
    rename_file $NEWFILE
    I=`expr $I + 1`
done
mv "$LOCALPATH$LOCALFILE" "$LOCALPATH$NEWFILE"
rsync "$LOCALPATH$NEWFILE" "$REMOTE$NEWFILE"
echo "$DOMAIN$NEWFILE" | xclip -selection clipboard
notify-send "Screenshot uploaded, URL in clipboard"
