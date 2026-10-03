#!/bin/sh
# Arma los samples de nana a partir de dead-wax-2005.wav (ver sintetizar.py):
#   dead-wax-2005.mp3 -> sample de audio
#   dead-wax-2005.mp4 -> sample de video (disco girando, 320x240 como la pantalla del nano)
set -e
cd "$(dirname "$0")"
F=/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf
python3 sintetizar.py
ffmpeg -y -loglevel error -i dead-wax-2005.wav -ac 1 -b:a 64k dead-wax-2005.mp3
# fondo: degradé de cielo 2005
convert -size 320x240 gradient:'#7fd1ff'-'#1e5fbf' fondo.png
# el disco: negro con surcos, etiqueta verde nano, agujero
convert -size 200x200 xc:none -fill '#111' -draw 'circle 100,100 100,2' \
  -fill none -stroke '#2a2a2a' -strokewidth 1 \
  -draw 'circle 100,100 100,8' -draw 'circle 100,100 100,14' -draw 'circle 100,100 100,20' \
  -draw 'circle 100,100 100,26' -draw 'circle 100,100 100,32' -draw 'circle 100,100 100,38' \
  -draw 'circle 100,100 100,44' -draw 'circle 100,100 100,50' \
  -stroke none -fill '#9acd32' -draw 'circle 100,100 100,66' \
  -fill '#d9f27a' -draw 'rectangle 70,92 130,96' \
  -fill '#fff' -draw 'circle 100,100 100,96' disco.png
ffmpeg -y -loglevel error -loop 1 -i fondo.png -loop 1 -i disco.png -i dead-wax-2005.wav -filter_complex "\
[1]rotate=a=t*3.49:c=none:ow=200:oh=200[r];\
[0][r]overlay=20:28[v1];\
[v1]drawbox=x=228:y=40:w=6:h=120:color=0xdddddd:t=fill,drawbox=x=212:y=150:w=22:h=10:color=0xbbbbbb:t=fill,\
drawtext=fontfile=$F:text='nana':fontsize=30:fontcolor=white:x=232:y=196:shadowx=1:shadowy=1,\
drawtext=fontfile=$F:text='sample de video':fontsize=11:fontcolor=white@0.85:x=232:y=224,\
drawtext=fontfile=$F:text='Dead Wax 2005':fontsize=14:fontcolor=white:x=12:y=8:shadowx=1:shadowy=1[v]" \
  -map "[v]" -map 2:a -t 25.7 -r 15 -c:v libx264 -preset veryslow -crf 30 -pix_fmt yuv420p -profile:v baseline \
  -c:a aac -b:a 64k -ac 1 -movflags +faststart dead-wax-2005.mp4
rm -f fondo.png disco.png dead-wax-2005.wav
ls -la
