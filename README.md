写在最前面：建议将所有cookie都更换成自己的

### 通用版：

这是一个有缺陷的、无依赖的版本，点击.exe文件即可使用。

缺陷就是部分图片无法被发现，自然也无法被下载。

### 完整版：

#### normal

通过谷歌的木偶 puppeteer， 我终于完成了。

但是有几个依赖项：

- node.js 主要为 node.exe， [下载地址](https://nodejs.org/en/)

    需要配置好 node.exe，百度完成即可。

- 依赖项 xxx.js ，是操纵木偶的 js，虽然py也可以，但是我没有首先获得这种方法，所以假装没看见，搞了个 js。

实现插画的下载，包括 R-18，但是太慢了。。。主要是木偶的问题。

对了，py还有一些库需要安装，到时候按照提示来就行了。

node.js 需要安装语法，并下载 puppeteer 库支持，具体命令如下：

~~~cpp
npm install express -g
npm install puppeteer
~~~

然后基本就可以使用了

#### cURL

这个可能比较快，但是还需要一个东西——curl， [下载地址](https://curl.haxx.se/windows/dl-7.72.0_3/curl-7.72.0_3-win64-mingw.zip)

然后将 /bin/ 目录加入环境变量。

然后就行了。



以上步骤没实践过，有误还望提醒。