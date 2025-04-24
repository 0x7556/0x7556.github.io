import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
### Author WebSite
### http://18k.icu
### https://blog.csdn.net/OneCrab
### https://github.com/0x7556
def download_images_from_url(url, save_dir=None):
    """
    从指定网页下载所有图片到本地指定目录。
    :param url: 网页URL
    :param save_dir: 图片保存目录（可选）
    """
    # 自动根据URL最后路由或文件名生成目录名
    if save_dir is None:
        parsed_url = urlparse(url)
        path = parsed_url.path.rstrip("/")
        dir_name = os.path.basename(path) if os.path.basename(path) else "images"
        save_dir = dir_name
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"获取网页失败: {e}")
        return
    soup = BeautifulSoup(resp.text, "html.parser")
    img_tags = soup.find_all("img")
    print(f"共发现{len(img_tags)}张图片")
    for idx, img in enumerate(img_tags, 1):
        img_url = img.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        ext = os.path.splitext(urlparse(img_url).path)[1]
        if not ext:
            ext = ".jpg"
        img_name = f"{idx}{ext}"
        save_path = os.path.join(save_dir, img_name)
        try:
            img_resp = requests.get(img_url, timeout=10)
            img_resp.raise_for_status()
            with open(save_path, "wb") as f:
                f.write(img_resp.content)
            print(f"已保存: {save_path}")
        except Exception as e:
            print(f"下载失败: {img_url} 错误: {e}")

def main():
    import sys
    if len(sys.argv) >= 2:
        url = sys.argv[1]
        download_images_from_url(url)
    else:
        print("用法: python download_images.py <url>")

if __name__ == "__main__":
    main()