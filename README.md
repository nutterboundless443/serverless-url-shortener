# 无服务器 URL 短链接服务

## 项目简介
这是一个基于无服务器架构的 URL 短链接生成服务，允许用户提交长链接，并生成一个短链接，方便分享和存储。

## 技术栈
- AWS Lambda：处理短链接生成的逻辑
- DynamoDB：存储长链接与短链接的映射关系
- API Gateway：提供 API 接口供用户调用
- S3：用于存储静态文件和前端页面

## 功能
- 提交长链接生成短链接
- 根据短链接重定向到原始长链接
- 查看历史生成的短链接

## 安装与部署
1. 克隆本项目到本地:
   ```bash
   git clone https://github.com/yourusername/serverless-url-shortener.git
   ```
2. 在 AWS 账户中配置 Lambda 和 API Gateway。
3. 使用 AWS SAM 或 Serverless Framework 部署服务。

## 贡献
欢迎任何形式的贡献！请查看 `CONTRIBUTING.md` 文件以了解更多信息。

## 许可证
MIT许可证。  
