#!pip install requests
# !pip install pandas
# pip install json
import requests
import pandas as pd
import json

url = "https://i.instagram.com/api/v1/users/web_profile_info"

querystring = {"username": "luvresval"}

payload = ""
headers = {
    "cookie": "csrftoken=0YDUxe0Rylnb47tomoF8QezT1ds5lWxF; shbid=%2214437%5C05445918412765%5C0541693487647%3A01f7222169e56225e4bedf8c85b40ae358dbf09ad24a5ef69d4f439f59e11e85bd8c4a33%22; shbts=%221661951647%5C05445918412765%5C0541693487647%3A01f75b61a1948a83e949d5e6317b53d5faa9c07f8b1f8b8f2f728f53219dcf057ca8201b%22; rur=%22LDC%5C05445918412765%5C0541693487647%3A01f7324d9ccf6dc95657fb626d0cf57ab94720f353d9a356d3a013aa7ee09d85d5d0ac51%22; ds_user_id=45918412765",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "X-CSRFToken": "0YDUxe0Rylnb47tomoF8QezT1ds5lWxF",
    "X-Instagram-AJAX": "1006124192",
    "X-IG-App-ID": "936619743392459",
    "X-ASBD-ID": "198387",
    "X-IG-WWW-Claim": "hmac.AR2ssCTC8yPV8kTRf2ye4xmWctVudrj6N5BZKL9cCudL-qPG",
    "Origin": "https://www.instagram.com",
    "Alt-Used": "i.instagram.com",
    "Connection": "keep-alive",
    "Referer": "https://www.instagram.com/",
    "Cookie": "csrftoken=0YDUxe0Rylnb47tomoF8QezT1ds5lWxF; mid=Yw5AigALAAEF3ly4J2UPhlwxKsYv; ig_did=83B4D439-47B2-4317-A4A1-3B50374C5477; ds_user_id=45918412765; sessionid=45918412765%3ALQIUW5AIjpprYJ%3A10%3AAYdKv1ISDRrmF3W5aXj_zDvMdua6FtajuIcrt3iPLA; shbid=14437\05445918412765\0541693414457:01f7132ca099010dfa00bed854983d008ae4a8fc582b6ce028c28ff32eced076e3746966; shbts=1661878457\05445918412765\0541693414457:01f76d3a7ccb336b13f279cdc1d328ba6effcf018c6763dc16618827ee660d22996d0787; datr=gHgOY9bKpi8oz3kK4rWshKhk; rur=LDC\05445918412765\0541693487555:01f7d5d89b49fcea9e6307f05b5e6603b95d1691cbf525b33aa84832f4cb0e6a77bb5ceb",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data = response.json()
user_data = data['data']['user']['edge_owner_to_timeline_media']['edges']

# create a JSON format
user_data_json = json.dumps(user_data, indent=4)

# normalize data
df = pd.json_normalize(user_data)
df.to_csv('result_game.csv', encoding='utf-8')

# filter the data that we want to use
result = pd.read_csv("result_game.csv", usecols=['node.id', 'node.video_view_count', 'node.edge_liked_by.count',
                                                 'node.edge_media_to_comment.count'])

# put the data from the csv into 4 array
video_id = [int(elem) for elem in result['node.id']]
like_per_video = [int(like) for like in result['node.edge_liked_by.count']]
comment_per_video = [int(comment) for comment in result['node.edge_media_to_comment.count']]
view_per_video = [str(view) for view in result['node.video_view_count']]

# show the result of the csv file
print(result.to_string())

for i in range(len(view_per_video)):
    view_per_video[i] = view_per_video[i].replace('.0', '')
view_per_video = list(map(int, [str(view) for view in view_per_video if view != 'nan']))
# print(f"{video_id}\n {like_per_video}\n {comment_per_video}\n{view_per_video}\n")
