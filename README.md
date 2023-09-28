# Hikari

Hikari是一个基于 FastAPI 开发、为动漫影视而生的 CMS 系统。

## 功能特点

- 提供动漫影视的管理功能，包括添加、编辑、删除等操作。
- 用户注册和登录功能，以及权限管理。
- 可插拔的插件系统，可以轻松扩展功能。
- ...

## 安装和运行

### 环境要求

- Python 3.9 或更高版本
- ...

### 安装依赖

使用 Poetry 进行依赖管理，确保已经安装 Poetry 工具。在项目根目录下运行以下命令安装依赖：

```shell
poetry install
```

### 配置

项目的配置文件为 `config.yaml`，请根据实际情况配置数据库连接等参数。

### 数据库初始化

运行以下命令初始化数据库：

```shell
python init.py
```

### 运行项目

运行以下命令启动项目：

```shell
poetry run uvicorn main:app --host 0.0.0.0 --port 8080
```

项目将在 `http://localhost:8080` 上运行。

## API 文档

API 文档基于 Swagger UI 自动生成，可以通过以下链接访问：

- [Swagger UI](http://localhost:8080/docs)：可交互的 API 文档。

## 插件开发

该项目支持插件开发，您可以在 `plugins` 文件夹中编写自己的插件，并将其添加到项目中。详细的插件开发指南，请参考 [插件开发文档](plugins/readme.md)。

## 贡献

欢迎您为该项目做出贡献！如果您发现问题或有改进建议，请提交 Issue 或 PR。

## 许可证

该项目基于 GPL-3.0-or-later 许可证。请查阅 [LICENSE](LICENSE) 文件了解详细信息。
```

```
项目正在维护中，待大更新
