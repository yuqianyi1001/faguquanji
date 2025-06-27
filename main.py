import requests
import os
import re


def set_script_location_as_working_directory():
    """Sets the script location as the working directory.

  Returns:
    The current working directory.
  """

    script_location = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_location)
    return os.getcwd()


def download_html_page_with_images(url):
    """Downloads an HTML page and all of its images.

  Args:
    url: The URL of the HTML page to download.

  Returns:
    A tuple of the HTML page and a dictionary of image URLs to image files.
  """

    print(f'html page: {url}')

    response = requests.get(url)
    html_page = response.content.decode("utf-8")
    with open(os.path.split(url)[-1], "w") as ff:
        ff.write(html_page)

    if not os.path.exists("img"):
        os.mkdir("img")

    image_urls = []
    for image_url in re.findall(r"<img style=\".*\" src=\"(.*?)\"", html_page):
        print(f'image: {image_url}')
        image_filename = os.path.basename(image_url)
        image_path = os.path.join("img", image_filename)

        if not os.path.exists(image_path):
            image_response = requests.get("https://ddc.shengyen.org/" + image_url)
            with open(image_path, "wb") as f:
                f.write(image_response.content)

        image_urls.append(image_path)

    return html_page, image_urls


# 准备步骤：
# 1. 从init_list.py中投入要下载的HTML页面列表。
# 2. 允许这个脚本下载html和图片。
# 3. 从m_json.py 中找到目录。 
# 4. 把目录整理成 合法的html格式，只需要保留href=具体的文件名称。
# 5. 把ul替换成ol。

# 制作
# 1. 在sigil中新建一个文件。
# 2. 导入所有html文件和图片。（只需要导入html文件，图片会自动导入。）
# 3. 在nav文件中的，<h1>Table of Contents</h1> 下面，粘贴目录（html片段）
# 4. 检查目录正常。
# 5. 设置metadata，语言，书名，作者。
# 6. 保存文件。

# 同步生成mobi和pdf文件
# 确认calibre已安装
# uv run ebook-helper.py 

if __name__ == '__main__':

    set_script_location_as_working_directory()

    toc = [

{'08-14-001.html': '編者序'},
{'08-14-002.html': '有情緒的人生才活得過癮？'},
{'08-14-003.html': '情緒從哪裡來？'},
{'08-14-004.html': '業力與潛意識'},
{'08-14-005.html': '如何安心？'},
{'08-14-006.html': '煩惱與習氣'},
{'08-14-007.html': '調和感性與理性'},
{'08-14-008.html': '什麼是貪心？'},
{'08-14-009.html': '為什麼貪心？'},
{'08-14-010.html': '轉貪心為願心'},
{'08-14-011.html': '以布施對治貪念'},
{'08-14-012.html': '名利只是暫時擁有'},
{'08-14-013.html': '遠離名位、權力的誘惑'},
{'08-14-014.html': '廣結善緣帶來好人緣'},
{'08-14-015.html': '凡事恰到好處最好'},
{'08-14-016.html': '清貧與慳吝大不同'},
{'08-14-017.html': '為什麼要生氣？'},
{'08-14-018.html': '瞋是心中火'},
{'08-14-019.html': '瞋心與慈心'},
{'08-14-020.html': '逆境要忍，順境也要忍'},
{'08-14-021.html': '生氣是慢性自殺'},
{'08-14-022.html': '忍耐不是忍氣吞聲'},
{'08-14-023.html': '別顛倒看世界'},
{'08-14-024.html': '煩惱與愚癡'},
{'08-14-025.html': '跳出自己設的陷阱'},
{'08-14-026.html': '危機就是轉機'},
{'08-14-027.html': '善用生命不懈怠'},
{'08-14-028.html': '不為自己找藉口'},
{'08-14-029.html': '讓生活重新上軌道'},
{'08-14-030.html': '是自信，還是自負？'},
{'08-14-031.html': '心存謙恭，樂當配角'},
{'08-14-032.html': '知慚愧才能更上進'},
{'08-14-033.html': '不懂就說不懂'},
{'08-14-034.html': '發現不足，包容別人'},
{'08-14-035.html': '謙虛才有成長空間'},
{'08-14-036.html': '慚愧不是自卑'},
{'08-14-037.html': '以鼓勵代替責備'},
{'08-14-038.html': '脫掉虛有其表的外衣'},
{'08-14-039.html': '如何消除虛榮心？'},
{'08-14-040.html': '該不該懷疑？'},
{'08-14-041.html': '疑心與信心'},
{'08-14-042.html': '用信來除疑'},
{'08-14-043.html': '疑出柳暗花明'},
{'08-14-044.html': '不要擔心未來'},
{'08-14-045.html': '怕也沒有用'},
{'08-14-046.html': '如何去除恐懼？'},
{'08-14-047.html': '無有恐怖'},
{'08-14-048.html': '自信度過每一天'},

         ]



    prefix = "https://ddc.shengyen.org/html/"

    for ii in toc:
        for k, v in ii.items():
            # print (k, v)

            #print(f'<li><a href="{k}">{v}</a></li>')

            download_html_page_with_images(prefix + k)

