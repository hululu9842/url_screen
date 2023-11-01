# -*- coding: utf-8 -*-
import re
import requests
import urllib3
import argparse

def parser():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("--domain",nargs='+',help='主域名,如 baidu.com，如果是多个，用空格隔开')
    parser.add_argument("--last",nargs='+',help='去掉图片等文件的url，如果是多个，用空格隔开,如使用 .png .jpg')
    parser.add_argument("--put", help='输入的url文件')
    parser.add_argument("--out", help='输出的url文件')
    args = parser.parse_args()
    return args


def get_code_status(urls_file,domain,last):
    """
    检测urls状态码
    :param urls_file: urls文件
    :return: 状态码
    allow_redirects: 拒绝默认的301/302重定向从而可以通过 html.headers[‘Location’] 拿到重定向的 URL。
    verify: 取消证书认证
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
    }
    domains = "|".join(domain)
    domains = domains.replace('.', '\.')
    lasts = "|".join(last)
    lasts = lasts.replace('.','\.')
    with open(urls_file, 'r', encoding='utf-8') as f:
        urls_data = f.readlines()
        result = ''
        for url in urls_data:
            ret_1 = re.findall(domains, url)  # 正则匹配主域名
            ret_2 = re.findall(lasts, url)  # 正则匹配文件url的后缀
            url = url.strip('\n')
            disable_warnings()
            try:
                res = requests.get(
                    url, headers=header, verify=False, allow_redirects=False
                )
            except Exception as error:
                print(error)
            code = res.status_code
            if code == 200:
                if ret_1!=[]:
                    if ret_2==[]:
                        print('状态码 {}:{}'.format(code, url))
                        result=result+''.join(url)+'\n'
    return result


def disable_warnings():
    """
    解除去掉证书后总是抛出异常告警
    """
    urllib3.disable_warnings()


if __name__ == '__main__':
    arg=parser()
    results=get_code_status(arg.put,arg.domain,arg.last)
    m = open(arg.out, 'w').write(results)

