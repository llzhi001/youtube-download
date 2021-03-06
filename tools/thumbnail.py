import os
import sys

# 生成size做前缀的缩略图（到子目录），然后可以根据缩略图名删除（移动）原视频

if len(sys.argv) != 2:
    print('参数错误')
    exit()

param = sys.argv[1]

filelist = []
if os.path.isfile(param):
    filelist.append(param)
elif os.path.isdir(param):
    filelist = os.listdir(param)

if not bool(filelist):
    print('参数错误')
    exit()

cmdtmpl = r'ffmpeg -loglevel quiet -ss 00:00:10 -nostdin -y -i "%s" -filter:v scale="640:-1" -vframes 1 "%s"'

counter = 0
for filepath in filelist:
    counter = counter + 1
    if not filepath.endswith('.webm'):
        continue
    thumbnail = filepath[:-5] + '.png'
    if os.path.isfile(thumbnail):
        print('%4.1f%% %d/%d '%(counter * 100 /len(filelist), counter, len(filelist)) + ' continue')
        continue
    cmd = cmdtmpl % (filepath, thumbnail)
    os.system(cmd)
    print('%4.1f%% %d/%d '%(counter * 100 /len(filelist), counter, len(filelist)) + filepath + ' done')