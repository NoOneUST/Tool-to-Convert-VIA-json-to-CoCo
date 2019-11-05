import json
import os

print('Author: WANG Likang\nEmail: lwangcg@connect.ust.hk')

annFile = 'via_export_coco.json'
annFileMem = json.load(open(annFile, 'r', encoding='utf-8'))
for i in range(annFileMem['annotations'].__len__()):
    annFileMem['annotations'][i]['image_id'] = int(
        annFileMem['annotations'][i]['image_id'])
    annFileMem['annotations'][i]['segmentation'] = [
        annFileMem['annotations'][i]['segmentation']]
with open(annFile[:-5] + '_processed.json', 'w', encoding='utf-8') as file:
    json.dump(annFileMem, file, ensure_ascii=False)

print('Done')

os.system('pause')
