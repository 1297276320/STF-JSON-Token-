import gradio as gr
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from transformers import AutoTokenizer
from tqdm import tqdm

# ✅ 自动选择系统自带的中文字体
def set_chinese_font():
    if os.name == "nt":  # Windows
        return "C:/Windows/Fonts/simsun.ttc"  # 使用宋体
    elif os.uname().sysname == "Darwin":  # macOS
        return "/System/Library/Fonts/Supplemental/Songti.ttc"  # macOS 宋体
    else:  # Linux
        return "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"  # Linux Noto 字体

# 设置 Matplotlib 字体
chinese_font_path = set_chinese_font()
plt.rcParams["font.family"] = fm.FontProperties(fname=chinese_font_path).get_name()
plt.rcParams["axes.unicode_minus"] = False  # 避免负号显示问题

# 加载 Qwen2.5 分词器
tokenizer = AutoTokenizer.from_pretrained(
    "Qwen2.5-0.5B-Instruct",
    trust_remote_code=True,
    use_fast=False
)

def process_json_file(file_path):
    """ 处理 JSON 文件，返回 DataFrame、CSV 文件、Token 分布统计 和 可视化图表 """
    
    # 读取 JSON 文件
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_entries = len(data)
    results = []

    # ✅ 终端 `tqdm` 进度条
    with tqdm(total=total_entries, desc="Processing JSON Data", unit="entry", mininterval=1) as term_pbar:
        for idx, entry in enumerate(data):
            # ✅ **减少终端进度条更新频率**（每 50 条更新一次）
            if idx % 50 == 0:
                term_pbar.update(50)  

            # ✅ 处理 JSON 数据
            instruction = entry.get("instruction", "")
            input_text = entry.get("input", "")
            output_text = entry.get("output", "")

            # Token 计算
            prompt_text = instruction + input_text
            prompt_token_length = len(tokenizer.tokenize(prompt_text))
            content_token_length = len(tokenizer.tokenize(output_text))
            total_num_tokens = prompt_token_length + content_token_length

            # Token 长度分区
            if total_num_tokens <= 10:
                token_range = "0-10"
            elif total_num_tokens <= 50:
                token_range = "11-50"
            elif total_num_tokens <= 100:
                token_range = "51-100"
            elif total_num_tokens <= 200:
                token_range = "101-200"
            elif total_num_tokens <= 500:
                token_range = "201-500"
            elif total_num_tokens <= 1000:
                token_range = "501-1000"
            elif total_num_tokens <= 1500:
                token_range = "1000-1500"
            elif total_num_tokens <= 2000:
                token_range = "1500-2000"
            elif total_num_tokens <= 2500:
                token_range = "2000-2500"
            elif total_num_tokens <= 3000:
                token_range = "2500-3000"
            else:
                token_range = "3000+"

            # ✅ 存储结果
            results.append({
                "instruction": instruction,
                "input": input_text,
                "output": output_text,
                "prompt_tokens_len": prompt_token_length,
                "content_tokens_len": content_token_length,
                "total_num_tokens": total_num_tokens,
                "Token Range": token_range
            })

    # ✅ **处理完成**
    df_results = pd.DataFrame(results)
    output_csv_path = "token_statistics.csv"
    df_results.to_csv(output_csv_path, index=False, encoding="utf-8-sig")

    # ✅ 计算 Token 长度分布
    token_dist, token_plot_path = analyze_token_distribution(df_results)

    return df_results, output_csv_path, token_dist, token_plot_path

def analyze_token_distribution(df):
    """ 统计不同 Token 长度的数据条数，并绘制可视化图表 """

    # 定义 Token 长度的区间
    bins = [0, 10, 50, 100, 200, 500, 1000, 1500, 2000, 2500, 3000, float("inf")]
    labels = ["0-10", "11-50", "51-100", "101-200", "201-500", "501-1000", "1000-1500", "1500-2000", "2000-2500", "2500-3000", "3000+"]

    # 统计不同 Token 长度的数量
    df["Token Range"] = pd.cut(df["total_num_tokens"], bins=bins, labels=labels, right=False)
    token_distribution = df["Token Range"].value_counts().sort_index()

    # 生成 Matplotlib 可视化
    plt.figure(figsize=(10, 6))
    token_distribution.plot(kind="bar")
    plt.xlabel("Token 长度区间")
    plt.ylabel("数据条数")
    plt.title("Token 长度分布")
    plt.xticks(rotation=45)
    plt.grid(axis="y")

    # 设置字体
    plt.xticks(fontproperties=fm.FontProperties(fname=chinese_font_path))
    plt.yticks(fontproperties=fm.FontProperties(fname=chinese_font_path))

    plt.savefig("token_distribution.png")  # 保存图表

    return token_distribution.to_dict(), "token_distribution.png"

# ✅ 创建 Gradio 界面
with gr.Blocks() as demo:
    gr.Markdown("# JSON 分词统计工具")

    with gr.Row():
        json_input = gr.File(label="上传 JSON 文件", type="filepath")  
        process_button = gr.Button("处理文件")

    output_table = gr.Dataframe(label="分词统计结果", wrap=True)
    download_link = gr.File(label="下载 CSV 结果", type="filepath")  
    token_distribution_output = gr.JSON(label="Token 长度分布统计")
    token_plot = gr.Image(label="Token 分布可视化图")

    process_button.click(process_json_file, 
                         inputs=[json_input], 
                         outputs=[output_table, download_link, token_distribution_output, token_plot])

# 启动 Gradio 服务器
if __name__ == "__main__":
    demo.launch(server_port=10010)
