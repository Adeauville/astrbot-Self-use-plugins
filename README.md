# sid‑private
AstrBot 管理员插件：群内执行 `/sid`，**群聊无任何输出，信息通过私聊静默返回**。

## ✨ 功能介绍
- 仅 **管理员** 可使用 `/sid` 指令
- 在**群聊**发送 `/sid`：群内不会输出任何消息，会话信息以私聊形式发送给执行指令的管理员
- 在**私聊**发送 `/sid`：直接在当前会话输出会话信息
- 返回内容：`session_id`、`user_id`、`group_id`（群聊）、平台名称
- 方便复制 session_id / group_id 用于 AstrBot 自定义规则配置

## 📜 指令
| 指令 | 权限 | 场景 | 效果 |
|---|---|---|---|
| `/sid` | 仅管理员 | 群聊 | 群内静默，私聊返回sid信息 |
| `/sid` | 仅管理员 | 私聊 | 当前会话直接输出sid信息 |

> 普通用户执行会提示：`❌ 只有管理员可以执行该指令`

## 📦 安装方式
### 方式1：AstrBot WebUI 直接安装（推荐）
1. 打开 AstrBot 管理面板 → 插件 → 安装插件
2. 填入本仓库 GitHub 地址，点击安装
3. 重载插件即可使用

### 方式2：手动安装
1. 下载本仓库源码
2. 将插件文件夹放到 `AstrBot/data/plugins/`
3. WebUI 重载插件，或者重启 AstrBot

## ⚠️ 注意事项
1. 机器人需要具备给管理员发送私聊消息的权限，否则群内调用 `/sid` 将无法收到返回信息
2. 仅支持 AstrBot Star 插件框架
3. 版本：`v1.0.0`
本人仅测试了QQ官方bot，需要@ bot再加上指令才能执行，小号bot没试过，不知道要不要@ bot才能执行，怕被封号不敢用小号部署。
<img width="337" height="68" alt="image" src="https://github.com/user-attachments/assets/a655e270-82e5-4072-8df0-b3c485721d14" />
<img width="263" height="137" alt="image" src="https://github.com/user-attachments/assets/19db342c-f175-408a-b0c8-1150a269bce3" />
