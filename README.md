### 介绍

WGEngine全称(Wap Game Engine), wap游戏引擎, 主要是为了方便简单的创建一个wap页游. 采用python + sanic实现. 并且大量使用中文变量名和方法,
降低学习成本(主要是懒的写注释和文档了,干脆直接用中文, 说实话,中文变量方法之类的还真不习惯)

### 目标

- [ ] 游戏框架
    - [ ] 页面
    - [ ] 技能
    - [ ] 战斗
    - [ ] 地图
    - [ ] 副本
    - [ ] 组队
    - [ ] NPC
    - [ ] 资源系统
    - [ ] GM管理端
- [ ] 游戏代码编辑器
    - [ ] 类vscode的编辑器
    - [ ] 支持语法解析
    - [ ] 支持实时预览
    - [ ] 支持与服务器同步
    - [ ] 支持图形化创建游戏资源
- [ ] 实现一门引擎专用游戏语言
    - [ ] 目前打算用python 实现
    - [ ] 设计语法与特性
    - [ ] 实现语法与特性
    - [ ] 实现与python完美互通

### 使用

**注意:** 现在还在开发中,但是由于工作原因,进度很慢,且开发时间也不稳定,暂时还只是个架子,还需要比较久,无法正常使用的,大家当个乐子就行.

#### 环境准备

- python >= 3.11
- mogodb
- redis

#### 修改配置

```shell
cp .env.example .env
```

然后修改.env中的信息为你本机的即可

#### 运行

```shell
# 没有安装poetry请先安装poetry
pip install poetry
poetry install
poetry shell
python server.py
```

### 致谢

- [html5tagger](https://github.com/sanic-org/html5tagger) - 一个可以用python写html页面的工具,本框架的页面引擎就是直接修改的html5tagger

### 联系

交流群(QQ): 946055169