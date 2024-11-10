# Flask 自动化工具项目

这是一个基于 Flask 的 Web 应用程序，集成了自动化工具功能。

## 功能特点

- 基于 Flask 框架开发的 Web 服务
- 完整的日志系统
  - 文件日志轮转
  - 控制台日志输出
  - 自定义日志格式

## 数据库
- 可以直接将数据库放在一个 Python 文件中然后导入使用

## 接口
- 可以参考 automa.py 文件中的写法，创建所需的接口
- 接口的注册可以参考 app.py 文件中的写法，创建蓝图然后注册
- automa 内已有接口暂时没有数据库及逻辑实现，需自行实现