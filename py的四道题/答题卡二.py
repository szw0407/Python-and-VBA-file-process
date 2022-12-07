import requests
import json


if __name__ == "__main__":
    try:
        OutFile=open("翻译结果.txt","a")
        
    except IOError as err:
        print("File error:"+str(err))
    while (1):
        msg = input()
        if msg=="":
            break
        dataobj = {
            "keyfrom": "node-fanyi",
            "key": "110811608",
            "type": "data",
            "doctype": "json",
            "version": "1.1",
            "q": msg
        }
        a = requests.post("https://fanyi.youdao.com/openapi.do", data=dataobj)

        try:
            res=json.loads(a.text)
        except json.JSONDecodeError:
            if str(a)=="<Response [500]>":
                print("ERROR:RESPONSE 500; TRY RUNNING THIS py FILE IN Linux TERMINAL")
            else:
                print("Unknown Error.")
        tran=res["translation"]
        
        OutFile.write(tran[0]+'\n')

