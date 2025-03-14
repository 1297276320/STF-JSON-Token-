# **STF JSON Token 统计工具**
🚀 **基于 Qwen2.5 分词器的 STF JSON 质量检测工具**

本项目使用 **Qwen2.5 分词器** 对 **STF 格式 JSON 文件** 进行 Token 统计，并可视化 Token 长度分布，以评估文本质量。支持 **Gradio Web UI** 交互，并提供 **CSV 下载**。

---

## 📌 **功能特性**
✅ **自动分词**：基于 **Qwen2.5 分词器** 进行文本分词  
✅ **Token 统计**：统计 `instruction`、`input`、`output` 的 Token 数量  
✅ **Token 长度区间分类**：
   - `0-10`
   - `11-50`
   - `51-100`
   - `101-200`
   - `201-500`
   - `501-1000`
   - `1000-1500`
   - `1500-2000`
   - `2000-2500`
   - `2500-3000`
   - `3000+`  
✅ **可视化数据**：生成 Token 长度分布的 **柱状图**  
✅ **CSV 导出**：统计结果可导出为 **CSV 文件**  
✅ **Gradio Web 界面**：支持文件上传、数据分析和结果下载  
✅ **支持中文**：自动设置 **Matplotlib 中文字体**，适配 Windows、Mac、Linux  

---

## 🔧 **安装与运行**
### 1️⃣ **环境要求**
**Python 版本**：Python 3.8 及以上  
**依赖库**：
```bash
pip install gradio transformers pandas matplotlib
```

---

### 2️⃣ **克隆仓库 & 运行**
```bash
# 克隆本仓库
git clone https://github.com/your-username/your-repo-name.git

# 进入项目目录
cd your-repo-name

# 运行项目
python main.py
```
运行后，访问 **[http://localhost:10010](http://localhost:10010)** 即可使用 **Web 界面**。

---

## 🎯 **使用方法**
1️⃣ **上传 STF 格式 JSON 文件**：
   - STF 文件示例：
     ```json
     [
       {
         "instruction": "介绍一下人工智能。",
         "input": "",
         "output": "人工智能是一种模拟人类智能的技术。"
       }
     ]
     ```
2️⃣ **点击 "处理文件" 按钮**：
   - 统计 `instruction + input` 的 Token 数量
   - 统计 `output` 的 Token 数量
   - 计算 **总 Token 数量**
   - **划分 Token 长度区间**
3️⃣ **查看 & 下载 Token 统计结果**：
   - Gradio 界面展示 **分词统计结果**
   - **CSV 文件可下载**
   - **柱状图可视化 Token 长度分布**

---

## 📊 **可视化结果**
- **Token 长度分布（柱状图）**
- **JSON 统计数据**
- **表格展示完整数据**
- **CSV 文件包含 `Token Range`**

示例 Token 统计表：
| instruction | input | output | prompt_tokens_len | content_tokens_len | total_num_tokens | Token Range |
|-------------|-------|--------|-------------------|--------------------|------------------|-------------|
| 介绍人工智能 |  | 人工智能是一种模拟人类智能的技术 | 5 | 10 | 15 | 11-50 |
| 解释机器学习 |  | 机器学习是AI的一个子领域 | 10 | 20 | 30 | 11-50 |
| 深度学习是什么 |  | 这是机器学习的一部分 | 15 | 40 | 55 | 51-100 |

---

## 📂 **项目结构**
```
📂 your-repo-name
 ├── main.py               # 主程序
 ├── requirements.txt      # 依赖库
 ├── README.md             # 说明文档
 ├── token_distribution.png # 可视化图表
 ├── token_statistics.csv   # 统计结果
```

---

## 🔗 **相关链接**
- **Qwen2.5 分词器**：[Qwen2.5 on Hugging Face](https://huggingface.co/Qwen2.5-0.5B-Instruct)
- **Gradio 文档**：[Gradio 官方文档](https://gradio.app/docs)
- **Matplotlib 中文支持**：[Matplotlib 中文字体教程](https://matplotlib.org/stable/tutorials/introductory/customizing.html)

---

## 🤝 **贡献**
欢迎提交 **Issue** 和 **PR** 以改进本项目！🎉

---

## 📜 **许可证**
本项目采用 **MIT License** 进行授权，欢迎自由使用和修改。
