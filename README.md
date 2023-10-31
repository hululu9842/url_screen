# url_screen

域名或url筛选工具

最近利用 JSFinder-master 扫描时，发现找到的很多url以及域名都不能用，所以写了一个很简单的python来简单解决一下，用来筛选200状态、需要的主域名以及去掉不必要的图片等的url。

通常配合 JSFinder-master使用。

仅供小白参考。

`python url_screen.py -h  ` 查看帮助

```
optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN [DOMAIN ...]
                        主域名,如 baidu.com，如果是多个，用空格隔开
  --last LAST [LAST ...]
                        去掉图片等文件的url，如果是多个，用空格隔开,如使用 .png .jpg
  --put PUT             输入的url文件
  --out OUT             输出的url文件
```

常用方法：

`python url_screen.py --domain xxx.com yyy.com --last .jpg .png .gif --put E:\url.txt --out E:\urls.txt`

![3p3aj7.png](https://files.catbox.moe/3p3aj7.png)