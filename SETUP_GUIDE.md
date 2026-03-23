# 测试用例生成工具 — 傻瓜式部署教程

本项目包含两个版本的测试用例生成工具，任选其一即可使用：

| 版本 | 说明 | 需要的 API Key |
|------|------|----------------|
| **网页版**（推荐） | Flask 网页应用，界面简洁美观 | Claude API Key |
| **桌面版** | Streamlit 应用，功能丰富，支持用例评审 | DeepSeek + 通义千问 API Key |

---

## 一、准备工作

### 1. 安装 Python

前往 [Python 官网](https://www.python.org/downloads/) 下载并安装 **Python 3.10 或以上版本**。

> **安装时务必勾选 "Add Python to PATH"**，否则后续命令无法执行。

安装完成后，打开终端（Windows 按 `Win + R`，输入 `cmd` 回车），验证安装：

```bash
python --version
```

如果显示类似 `Python 3.12.x` 就说明安装成功。

### 2. 下载项目代码

**方式一：Git 克隆（推荐）**

```bash
git clone https://github.com/kinmingyu448-ui/AutoGenTestcase.git
cd AutoGenTestcase
```

**方式二：直接下载**

1. 打开 https://github.com/kinmingyu448-ui/AutoGenTestcase
2. 点击绿色的 `Code` 按钮 → `Download ZIP`
3. 解压到任意目录，进入解压后的文件夹

---

## 二、网页版（Flask）— 推荐

这是一个简洁的网页工具，输入需求文档即可生成测试用例。

### 第 1 步：安装依赖

在项目根目录打开终端，执行：

```bash
pip install flask anthropic python-docx
```

> 如果 `pip` 报错，试试 `pip3` 或 `python -m pip install flask anthropic python-docx`

### 第 2 步：启动服务

```bash
cd webapp
python app.py
```

看到以下输出就说明启动成功：

```
 * Running on http://0.0.0.0:5000
```

### 第 3 步：打开网页

浏览器访问：

```
http://localhost:5000
```

### 第 4 步：使用

1. 在页面顶部输入你的 **Claude API Key**（以 `sk-ant-` 开头）
2. 在「需求文档」区域粘贴需求文本，或上传 `.docx` / `.txt` 文件
3. （可选）粘贴技术文档、上传设计稿图片
4. 点击 **「生成测试用例」** 按钮
5. 等待 AI 生成完毕，可以复制内容或下载 `.md` 文件

### Claude API Key 获取方法

1. 打开 https://console.anthropic.com/
2. 注册并登录
3. 进入 `API Keys` 页面，创建一个新的 Key
4. 复制 Key，粘贴到网页中使用

> Claude API 为付费服务，需要在 Anthropic 官网绑定支付方式后才能使用。

---

## 三、桌面版（Streamlit）

基于 Streamlit 构建的桌面交互界面，支持 DeepSeek 编写用例 + 通义千问评审用例的多角色协作模式。

> **注意：桌面版仅支持 Windows 系统。**

### 第 1 步：安装依赖

```bash
pip install streamlit autogen-agentchat autogen-ext[openai] xlsxwriter
```

### 第 2 步：配置 API Key

用文本编辑器打开项目根目录下的 `config.ini` 文件，填入你的 API Key：

```ini
[deepseek]
api_key = 你的DeepSeek API Key

[qwen]
api_key = 你的通义千问 API Key
```

### 第 3 步：启动应用

```bash
python run.py
```

浏览器会自动打开页面。如果没有自动打开，手动访问终端中显示的地址（通常是 `http://localhost:8501`）。

### 第 4 步：使用

1. 在「AI模型设置」标签页检查模型配置，确认 API Key 已填入
2. 切换到「AI交互」标签页
3. 上传 `.txt` 需求文件或手动输入需求描述
4. （可选）调整高级选项：用例分类占比、优先级、数量
5. 点击 **「生成测试用例」**
6. 生成完毕后可下载 `.md` 或 `.xlsx` 文件

### API Key 获取方法

**DeepSeek：**
1. 打开 https://platform.deepseek.com/api_keys
2. 注册账号并登录
3. 创建 API Key
4. 充值少量金额即可使用（约 2 元可用上百次）

**通义千问：**
1. 打开 https://bailian.console.aliyun.com/?tab=model#/api-key
2. 用支付宝账号登录即可
3. 创建 API Key
4. 新用户赠送百万 tokens，足够使用

---

## 常见问题

### Q: `pip install` 报错 / 下载很慢？

使用国内镜像源加速：

```bash
pip install flask anthropic python-docx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q: 启动后访问 `localhost:5000` 显示无法访问？

- 确认终端中没有报错信息
- 确认没有其他程序占用 5000 端口
- 尝试访问 `http://127.0.0.1:5000`

### Q: Claude API 报错 "API Key 无效"？

- 确认 Key 以 `sk-ant-api03-` 开头
- 确认 Anthropic 账户已绑定支付方式并有余额

### Q: 桌面版提示 "不支持当前系统"？

桌面版（Streamlit）仅支持 Windows 系统，Mac/Linux 用户请使用网页版（Flask）。

---

## 项目结构

```
├── webapp/                  # 网页版（Flask）
│   ├── app.py              # Flask 主程序
│   ├── requirements.txt    # Python 依赖
│   ├── system_prompt.txt   # AI 系统提示词
│   ├── static/style.css    # 页面样式
│   └── templates/index.html # 页面模板
├── page.py                 # 桌面版主界面（Streamlit）
├── run.py                  # 桌面版启动入口
├── llms.py                 # 模型配置
├── config.ini              # 桌面版模型参数配置
├── TESTCASE_WRITER_SYSTEM_MESSAGE.txt  # 用例编写提示词
├── TESTCASE_READER_SYSTEM_MESSAGE.txt  # 用例评审提示词
└── 需求文档示例.txt          # 示例需求文档
```
