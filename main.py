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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    set_script_location_as_working_directory()

    toc = [
      {'09-10-001.html': '自序'},
{'09-10-002.html': '落髮的意義'},
{'09-10-003.html': '和闖．和樣與和尚'},
{'09-10-004.html': '男女．僧俗．內外之分'},
{'09-10-005.html': '守己與守分'},
{'09-10-006.html': '除夕夜好懺悔'},
{'09-10-007.html': '居安思危'},
{'09-10-008.html': '穩固出家的心態'},
{'09-10-009.html': '調適身心'},
{'09-10-010.html': '心不隨境轉'},
{'09-10-011.html': '彼此體諒．互相關懷'},
{'09-10-012.html': '學佛的清淨三業'},
{'09-10-013.html': '海綿精神'},
{'09-10-014.html': '拜佛懺悔求安心'},
{'09-10-015.html': '煩惱消歸自心'},
{'09-10-016.html': '多念佛．勤拜佛．堅固信心'},
{'09-10-017.html': '保重身體'},
{'09-10-018.html': '安心的方法'},
{'09-10-019.html': '愛惜常住'},
{'09-10-020.html': '依共住規約而住'},
{'09-10-021.html': '法統和僧倫'},
{'09-10-022.html': '以師父為中心'},
{'09-10-023.html': '如何適應常住的生活'},
{'09-10-024.html': '依眾靠眾'},
{'09-10-025.html': '謹言慎口'},
{'09-10-026.html': '師兄弟相處之道'},
{'09-10-027.html': '尊戒、盡分'},
{'09-10-028.html': '以和成事．以敬安人'},
{'09-10-029.html': '僧事僧斷'},
{'09-10-030.html': '團體的成功就是個人的成功'},
{'09-10-031.html': '和光同塵的僧團'},
{'09-10-032.html': '對供養物品的處理'},
{'09-10-033.html': '接待禮節'},
{'09-10-034.html': '規約與恆課'},
{'09-10-035.html': '禮儀和威儀'},
{'09-10-036.html': '課誦與拜佛'},
{'09-10-037.html': '梵唄和修行'},
{'09-10-038.html': '供養的意義'},
{'09-10-039.html': '開會的意義與素養'},
{'09-10-040.html': '私取僧物造生死業'},
{'09-10-041.html': '出家生活——入眾、隨眾、依眾、靠眾'},
{'09-10-042.html': '神聖的僧中執事'},
{'09-10-043.html': '執事者應具備的觀念'},
{'09-10-044.html': '執事的共識——以和為貴'},
{'09-10-045.html': '執事的原則和方法'},
{'09-10-046.html': '僧眾平等、僧俗有別'},
{'09-10-047.html': '僧中執事即是修行'},
{'09-10-048.html': '侍者'},
{'09-10-049.html': '如何統理大眾'},
{'09-10-050.html': '整體的僧團'},
{'09-10-051.html': '新的執事，新的挑戰'},
{'09-10-052.html': '執事是激發潛在才智的機會'},
{'09-10-053.html': '執事是常住三寶所付予的'},
{'09-10-054.html': '執事要有整體觀'},
{'09-10-055.html': '在接受批評、指責、檢討中成長'},
{'09-10-056.html': '回歸佛陀本懷'},
{'09-10-057.html': '菩薩行者的修學'},
{'09-10-058.html': '佛教的大愛'},
{'09-10-059.html': '佛道與非佛道'},
{'09-10-060.html': '危機與轉機'},
{'09-10-061.html': '心的層次'},
{'09-10-062.html': '森林中的共命鳥'},
{'09-10-063.html': '以師父的悲願為悲願'},
{'09-10-064.html': '夢中說夢'},
{'09-10-065.html': '法鼓山僧團'},
{'09-10-066.html': '我的方向——做好出家人的本分'},
{'09-10-067.html': '我們的願景'},
{'09-10-068.html': '校註'},      
         ]



    prefix = "https://ddc.shengyen.org/html/"

    for ii in toc:
        for k, v in ii.items():
            # print (k, v)

            #print(f'<li><a href="{k}">{v}</a></li>')

            download_html_page_with_images(prefix + k)

