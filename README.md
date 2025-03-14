# STF JSON Token 统计工具

本项目利用 **Qwen2.5** 的分词器，对 **STF 格式** 的 JSON 文件进行 Token 统计，以便检测文本质量。该工具使用 **Gradio** 提供可视化界面，并支持生成 Token 统计的 **CSV 文件**。

## ✨ 功能特性

- **自动分词**：使用 **Qwen2.5 分词器** 对 JSON 文件中的文本进行分词。
- **Token 统计**：计算 `instruction`、`input` 和 `output` 部分的 Token 数量。
- **CSV 导出**：统计结果可导出为 **CSV 文件** 方便分析。
- **Gradio 界面**：提供 **Web UI**，支持文件上传和下载。

---

## 🚀 安装 & 运行

### 1️⃣ 环境要求

确保你的 Python 版本为 **3.8+**，并安装以下依赖库：

```bash
pip install gradio transformers pandas
```

---

### 2️⃣ 下载 & 运行

```bash
# 克隆本仓库
git clone https://github.com/your-username/your-repo-name.git

# 进入项目目录
cd your-repo-name

# 运行项目
python main.py
```

程序启动后，访问 [http://localhost:10010](http://localhost:10010) 即可使用 Web 界面。

---

## 📌 使用方法

1. **上传 STF 格式 JSON 文件**：
   - 文件应包含 `instruction`、`input` 和 `output` 字段。
   - 示例：
     ```json
     [
       {
         "instruction": "介绍一下人工智能。",
         "input": "",
         "output": "人工智能是一种模拟人类智能的技术。"
       }
     ]
     ```

2. **点击 "处理文件" 按钮**：
   - 统计 `instruction + input` 的 Token 数量。
   - 统计 `output` 的 Token 数量。
   - 计算总 Token 数量。

3. **查看 & 下载 Token 统计结果**：
   - 统计结果将在界面上展示。
   - 可下载 **CSV 文件** 进行进一步分析。

---

## 📝 代码结构

```
📂 your-repo-name
 ├── main.py               # 主程序
 ├── requirements.txt      # 依赖库
 ├── README.md             # 说明文档
```

---

## 🔗 相关链接

- **Qwen2.5 分词器**：[Qwen2.5 on Hugging Face](https://huggingface.co/Qwen2.5-0.5B-Instruct)
- **Gradio 文档**：[Gradio 官方文档](https://gradio.app/docs)

---

## 🤝 贡献

欢迎提交 **Issue** 和 **PR** 以改进本项目！🎉

---

## 📜 许可证

本项目使用 **MIT License** 进行授权，欢迎自由使用和修改。
