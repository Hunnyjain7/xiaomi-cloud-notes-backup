import json
import os
import re
import requests

# Add Your cookies here after manually login into https://i.mi.com/ copy the request headers and use it here
cookies = "xm_user_bucket=7; _gid=GA1.2.1126272325.1715417103; _gcl_au=1.1.1112427708.1715417104; utmMedium=organic; xmuuid=XMGUEST-CE80D815-6109-DEAE-078D-DBAFD807387E; _fbp=fb.1.1715417104321.2115791754; moe_uuid=44524221-a5ab-4320-8516-00331c65051d; OPT_IN_SHOWN_TIME=1715417105759; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; cUserId=KqOaYZR7fMVWUeGvVrjWKH2hQfw; mUserId=rAHvEJJTK7OERKYA9%2BJ%2FhH6s363hgL72oW0HMxt6jns%3D; xm_order_btauth=5799be7bebe8003f5a8e726a5dde6c77; guserid=cd47023b6a6c1b1479e93a0ac5e32638; userId=5153449943; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%225153449943%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2244524221-a5ab-4320-8516-00331c65051d%22%2C%22deviceAdded%22%3Atrue%7D; __utma=127562001.631882573.1715417103.1715417138.1715417138.1; __utmc=127562001; __utmz=127562001.1715417138.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_E3SLZ98203=GS1.2.1715417160.1.0.1715417160.60.0.0; _ga_EL454QDSPM=GS1.1.1715417104.1.1.1715417241.0.0.0; _ga=GA1.1.631882573.1715417103; SESSION=%7B%22sessionKey%22%3A%226b5adf0e-284f-45e9-b2e8-046c1ae73a6b%22%2C%22sessionStartTime%22%3A%222024-05-11T08%3A45%3A04.718Z%22%2C%22sessionMaxTime%22%3A1800%2C%22sessionEnabled%22%3A%22allowed%22%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1715419042037%2C%22numberOfSessions%22%3A1%7D; _ga_YYVZDLF0XE=GS1.1.1715417104.1.1.1715417245.54.0.0; uLocale=en_US; iplocale=en_IN; i.mi.com_isvalid_servicetoken=true; i.mi.com_ph=uzVLVHsY+uT4sHrvnCPdwQ==; i.mi.com_istrudev=true; serviceToken=jNa2f6UlbQ0iiMIayebNzd2xLGnBjv3aib/4XrCQVOXz7Tr+ImFXI2I6PPhtneEUp98qDdDmZ+//DoxArRI8p30SIfAbRqbRFaPxvxan3DRjX5KB31JrG1knvICUo+bK2ZWRfnlI5OsF9mlsKmia27Iqx1j8jWm4pZpVQnEb/xnqDhyUYXn4zhd+Ts03/DTg5iYS0N1MbjfrGWNPbecpONpsrn2QfLgnWMiB7IqAg1BdvKPayb8g5XB+EtKfx8WS3Gf0GEIPBpprtyjo3hQVSAOKk5xLrDP5DUvqXN47GEeD9U2OGt8S3TT5S/FMkPRLsZNZha91MLX6Qu67qhIotjJJaMTMkywnBtSz3UlfsLoFCg0XvUZhY8g4O9vD50EK1G6oWjSzb8syOQ2jUkDrQA==; i.mi.com_slh=w6ObYeMu5tGfpgsqHjVNVjwyzXA="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "cookie": cookies,
}
main_data = requests.request(
    url="https://in.i.mi.com/note/full/page/?syncTag=34179980214935584&limit=2000", method='get',
    headers=headers
).json()


# Function to remove HTML/XML-like tags from a string
def remove_tags(text):
    # Regular expression to find and replace tags
    cleaned_text = re.sub(r'<[^>]+>', '', text)
    return cleaned_text


base_folder = "Notes"
cwd = os.getcwd()  # Get the current working directory
if base_folder not in os.listdir(cwd):
    os.mkdir(base_folder)

file_names = set()
for entry in main_data.get("data", {}).get("entries", []):
    note_id = entry.get("id", "")
    note_data = requests.request(
        url=f"https://in.i.mi.com/note/note/{note_id}/",
        method='get',
        headers=headers
    ).json().get("data", {}).get("entry", {})
    content = note_data.get("content", "")
    title = json.loads(note_data.get("extraInfo", {})).get("title")
    if content.strip().startswith("<text "):
        content = remove_tags(content)

    file_name = f"file_{note_id}" if not title or title in file_names else title.strip()
    with open(f"{base_folder}/{file_name}.txt", "w", encoding='utf-8') as f:
        f.write(content)
        f.close()
        print(f"Took the backup of {file_name}.txt")

print("Backup Completed.")
