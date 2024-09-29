def send(token:str, message:str) -> None :
  import requests
  URL = "https://notify-api.line.me/api/notify"
  headers = {"Authorization": f"Bearer {token}"} # headersを変数に定義
  payload = {"message": message} # payloadを変数に定義
  requests.post(url=URL,headers=headers,params=payload)

def img_send(token:str, message:str, image_path:str|None) -> None :
  import requests
  URL = "https://notify-api.line.me/api/notify"
  headers = {"Authorization": f"Bearer {token}"} # headersを変数に定義
  payload = {"message": message} # payloadを変数に定義
  if not image_path == None :
    image = {'imageFile': open(image_path, 'rb')}
  requests.post(
    url=URL,
    headers=headers,
    params=payload,
    files=image
    )

def sticker_send(token:str, message:str, stickerPackageID:int, stickerId:int) -> None :
  import requests
  URL = "https://notify-api.line.me/api/notify"
  headers = {"Authorization": f"Bearer {token}"} #  headersを変数に定義
  payload = {
    "message": message,
    "stickerPackageID": stickerPackageID, # payloadを変数に定義
    "stickerId": stickerId
    }
  requests.post(url=URL,headers=headers, params=payload)
