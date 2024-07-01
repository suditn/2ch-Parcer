import requests
import os
import urllib




def extract(html_text):
#    response = requests.get(url)
    data_url = []
    searchstr = 'data-url='
    for line in html_text.split("\n"):
        #print(line)
        for lines in line.split(" "):
            if searchstr in lines:
                data_url.append(lines.split("\"")[1])
    return data_url
def get_html(url):
    data_url = []
    if requests.get(url).status_code == 200:
        print("Тред существует\n")
    else:
        print("Треда нет\n")
    html_get = requests.get(url)
    data_url = extract(html_get.text)
    #print(data_url)
    return data_url

def parser_data(url_video):
    print("Начинаю скачивания видео\n")
    if not os.path.exists("content"):
        os.makedirs("content")
        print("Папка была создана, начинаю загрузку файлов\n")
    else:
        print("Начинаю загрузку файлов\n")
    for video in url_video:
        print("Файл https://2ch.hk"+video)
        if not os.path.exists("content/"+video.split("/")[-1]):
            with open("content/"+video.split("/")[-1], 'wb') as v:
                v.write(requests.get("https://2ch.hk"+video).content)
                print("\nФайл сохранён\n")
        else:
            print("Файл "+video.split("/")[-1] + " существует")


def main():
    url = input("Введите ссылку на тред\n->")
    parser_data(get_html(url))


main()
