#!/bin/bash
# based on GtkGrab by @EvanDotPro https://github.com/EvanDotPro/GtkGrab
function rename_file()
{
    NEWFILE=$(echo $1 | md5sum | cut -c-25)'.png'
}
REMOTE=inyuki@mindey.com:/home/inyuki/webapps/cv/screens/
DOMAIN=https://mindey.com/screens/
LOCALPATH=/home/mindey/Pictures/Screenshots/
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
