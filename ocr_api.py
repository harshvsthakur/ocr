import requests
import json, re
import os, time

def ocr_space_file(filename, overlay=False,
                   api_key='', # Enter API Key here
                   language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


# Use examples:

folder = r"Scan"

for files in os.listdir(folder):
    if ".pdf" in files:
        test_file = ocr_space_file(filename=os.path.join(os.path.abspath(folder),files),
                                   language='eng')
        x = json.loads(test_file)
        try:
            text = x["ParsedResults"][0]["ParsedText"]
            POnum = "".join(re.findall(r"(MEP+[^\s]+)",text))[-5:]
            vid_pattern = POnum + r"(\r\n|\r|\n)+.\d.+(\r\n|\r|\n)+([^\s]+)"
            VID = re.findall(vid_pattern, text)[-1]
            jid_pattern = r"S|supplier.+(\r\n|\r|\n)+(\w.+[^\s])"
            JID = re.findall(jid_pattern,text)
            for i in JID:
                for j in i:
                    if len(j) > 3:
                        JID = j

            print (POnum, VID[-1][-5:], JID)
        except:
            print("oops")

# test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')
