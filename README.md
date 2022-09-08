![up-low-letter](https://socialify.git.ci/surrtr/up-low-letter/image?description=1&descriptionEditable=%E6%9C%89%E8%B6%A3%E7%9A%84Python%E8%84%9A%E6%9C%AC%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%A4%A7%E5%B0%8F%E5%86%99&font=Bitter&forks=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fsurrtr%2Fup-low-letter%2Fab8449ab87be55364e8d71ab25ba9dc93cd1ca45%2Fassets%2FUL_icon.png&name=1&pattern=Plus&stargazers=1&theme=Light)

简体中文 | [繁體中文]() | [English]()

## 起因

由于我在打英文的时候，经常出现忘记按`Shift`或者按了`Shift`后变成中文当场炸裂，出现`eve`变成`vev`等情况，所以整活搞了一个这么一个玩意，就当练手。

## 可能的警告

如果您在使用时使用的是非苹果设备，脚本可能会出现警告：

```warning
WARNING: It seems like you're using a non-Apple device, which is not cool!
```

这是因为本项目已经加入ADRO（Apple Device Remind Organization缩写，苹果设备提醒组织），我们致力于让世界用上更好的平台（~~Linux天下第一，不接受反驳~~）

优秀同组织项目：[helang(何语言，次世代赛博编程语言。)](https://github.com/kifuan/helang)

所以.........关注苟蝙蝠大帝，关注弗里德里希苟蝙蝠大帝，关注prussia大帝苟蝙蝠谢谢喵~[^1]

## To do

- [x] 实现从文件读取

- [x] 实现写入结果到文件

- [x] 实现命令行参数无键入顺序限制

- [x] 加入ADRO(Apple Device Remind Organization)

- [ ] 发布独立的汉语版本（现在提示语为英语，包括help和提示语）

## 参数

| 参数  | 用法          | 冲突（一起使用将出现冲突） | 描述      |
| --- | ----------- | ------------- | ------- |
| -h  | -h          | ✓             | 获取帮助    |
| -f  | -f <文件名>    | ✓             | 读取文件以转换 |
| -t  | -t '<你的文本>' | ✓             | 转换指定字符  |
| -o  | -o <输出路径>   |               | 输出结果为文件 |

注意：同时使用`-h`与其他参数可能不会报错，她将**直接传回帮助！！！**

## 使用方法

1. 下载仓库到本地（使用git）
   
   ```bash
   git clone https://github.com/surrtr/up-low-letter.git
   ```

2. 使用脚本
   
   ```bash
   python 114514.py [参数]
   ```

3. 享受她~~

## 特别感谢

- [meinming](https://github.com/meinming) （~~我谢我自己 大雾~~）

## 附加

现在是11:37，我为自己点了一份外卖

Apple 和 AirPods 是 Apple Inc. 在美国和其他国家和地区注册的商标。

Shot on Marktext,Windows,By meinming

[^1]:苟蝙蝠，一个精普UP，我们的普鲁士国王，详细见[这里](https://www.bilibili.com/video/av759170665)
