#!/bin/bash
# based on GtkGrab by @EvanDotPro https://github.com/EvanDotPro/GtkGrab
function compress_file()
{
    NEWFILE=$(echo $1 | md5sum | cut -c-25)'.mp4'
}
REMOTE=mindey@wiki.mindey.com:/home/mindey/shared/shots/
DOMAIN=https://wiki.mindey.com/shared/shots/
LOCALPATH=/home/mindey/Media/Shots/
# UNIMPLEMENTED recordscreen.py -r --save=$LOCALPATH
LOCALFILE=$(ls -tr $LOCALPATH | tail -n 1)
compress_file $LOCALFILE
