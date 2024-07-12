import requests
import os
import urllib




def extract(html_text, url):
#    response = requests.get(url)
    data_url = []
    op_text = []
    searchstr = 'data-url='
    op_url = url.split("/")[-1]
    op = op_url.split(".html")[0]
    serchstr2 = '<article id="m' + op + '" class="post__message post__message_op">'
    #<article id="m306793097" class="post__message post__message_op">
    print(serchstr2)
    for line in html_text.split("\n"):
        #print(line)
        for lines in line.split(" "):
            if searchstr in lines:
                data_url.append(lines.split("\"")[1])
    for line in html_text.split(serchstr2):
        op_text.append(line.split("</article>")[0])
    print(op_text[-1][0:50])
    return data_url, op_text[-1]
def get_html(url):
    data_url = []
    if requests.get(url).status_code == 200:
        print("Тред существует\n")
    else:
        print("Треда нет\n")
    html_get = requests.get(url)
    #print(html_get.text)
    data_url = extract(html_get.text, url)
    #print(data_url)
    return data_url

def parser_data(url_video, name_folder):
    print("Начинаю скачивания видео\n")
    new_name_folder = ""
    new_name_folder = name_folder.translate(str.maketrans('', '', "\\/<br><em>"))
    print(new_name_folder)
    if not os.path.exists(new_name_folder[1:20]):
        os.makedirs(new_name_folder[1:20])
        print("Папка была создана, начинаю загрузку файлов\n")
    else:
        print("Начинаю загрузку файлов\n")
    for video in url_video:
        print("Файл https://2ch.hk"+video)
        if not os.path.exists(new_name_folder[1:20]+"/"+video.split("/")[-1]):
            with open(new_name_folder[1:20]+"/"+video.split("/")[-1], 'wb') as v:
                v.write(requests.get("https://2ch.hk"+video).content)
                print("\nФайл сохранён\n")
        else:
            print("Файл "+video.split("/")[-1] + " существует")


def main():
    url = input("Введите ссылку на тред\n->")
    url_video, name_folder = get_html(url)
    parser_data(url_video, name_folder)


main()
