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
      {'07-11-001.html': '編者序'},
      {'07-11-002.html': '修四念處的究竟目標——智慧'},
      {'07-11-003.html': '身念處'},
      {'07-11-004.html': '受念處'},
      {'07-11-005.html': '心念處'},
      {'07-11-006.html': '法念處'},
      {'07-11-007.html': '大乘觀空的方法'},
      {'07-11-008.html': '前言'},
      {'07-11-009.html': '四正勤是三十七道品的內容之一'},
      {'07-11-010.html': '四正勤的異名'},
      {'07-11-011.html': '善法與惡法'},
      {'07-11-012.html': '四正勤的內容'},
      {'07-11-013.html': '修行四正勤在大小乘的重要性'},
      {'07-11-014.html': '精進的種類'},
      {'07-11-015.html': '佛教基本三經皆重視精進行'},
      {'07-11-016.html': '結論'},
      {'07-11-017.html': '四如意足是四種定境'},
      {'07-11-018.html': '修證次第中的四如意足'},
      {'07-11-019.html': '四如意足的內容'},
      {'07-11-020.html': '四如意足即是四種三摩地'},
      {'07-11-021.html': '四如意足即是四神足'},
      {'07-11-022.html': '四如意足為何稱為四神足'},
      {'07-11-023.html': '四神足不是神足通'},
      {'07-11-024.html': '前言'},
      {'07-11-025.html': '何謂五根及五力？'},
      {'07-11-026.html': '如何在日常生活中運用五根？'},
      {'07-11-027.html': '五力的功用'},
      {'07-11-028.html': '五根五力的經證及論證'},
      {'07-11-029.html': '問答'},
      {'07-11-030.html': '三十七道品第六科'},
      {'07-11-031.html': '何謂七覺支？'},
      {'07-11-032.html': '七覺支的意義'},
      {'07-11-033.html': '《阿含經》中的七覺支修持及其功用'},
      {'07-11-034.html': '大乘經論中的七覺支'},
      {'07-11-035.html': '何謂八正道？'},
      {'07-11-036.html': '八正道的地位'},
      {'07-11-037.html': '八正道是捨苦樂二邊的中道行'},
      {'07-11-038.html': '八正道的定義'},
      {'07-11-039.html': '八正道的內容'},
      {'07-11-040.html': '八正道與三增上學'},
      {'07-11-041.html': '八正道與四聖諦'},
      {'07-11-042.html': '八正道與十二因緣'},
      {'07-11-043.html': '八正道是三乘共法'},
      {'07-11-044.html': '八正道即為大乘佛法'},
      {'07-11-045.html': '出離三界的八正道'},
      {'07-11-046.html': '附錄 英文版《菩提之道——三十七道品》編者序'},
      {'07-11-047.html': '校註'},    ]



    prefix = "https://ddc.shengyen.org/html/"

    for ii in toc:
        for k, v in ii.items():
            # print (k, v)

            #print(f'<li><a href="{k}">{v}</a></li>')

            download_html_page_with_images(prefix + k)
