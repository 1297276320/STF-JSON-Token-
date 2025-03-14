import gradio as gr
import os
import json
import pandas as pd
from transformers import AutoTokenizer

# 加载 Qwen2.5 分词器
tokenizer = AutoTokenizer.from_pretrained(
    "Qwen2.5-0.5B-Instruct",
    trust_remote_code=True,
    use_fast=False
)

def process_json_file(file_path):
    """ 处理 JSON 文件，返回分词统计结果和 CSV 文件路径 """

    # 读取 JSON 文件
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 存储分词结果
    results = []
    
    for entry in data:
        # 获取 entry 中的字段
        instruction = entry.get("instruction", "")
        input_text = entry.get("input", "")
        output_text = entry.get("output", "")
        
        # token_id 编码
        prompt_text = instruction + input_text  # 传入值拼接
        prompt_token_ids = tokenizer.encode(prompt_text)  # 给输入文本编码
        content_token_ids = tokenizer.encode(output_text)  # 给输出文本编码

        # 计算 token 长度
        prompt_tokens = tokenizer.tokenize(prompt_text)  # 对 prompt_text 进行分词
        prompt_token_length = len(prompt_tokens)
        content_tokens = tokenizer.tokenize(output_text)  # 对 output_text 进行分词
        content_token_length = len(content_tokens)
        total_num_tokens = prompt_token_length + content_token_length  # 总 token 数量

        # 保存结果
        results.append({
            "instruction": instruction,
            "input": input_text,
            "output": output_text,
            "prompt_tokens_len": prompt_token_length,
            "content_tokens_len": content_token_length,
            "total_num_tokens": total_num_tokens,
        })

    # 转换为 DataFrame
    df_results = pd.DataFrame(results)
    
    # 生成 CSV 文件路径
    output_csv_path = "token_statistics.csv"
    df_results.to_csv(output_csv_path, index=False, encoding="utf-8-sig")

    return df_results, output_csv_path

# Gradio 界面
def gradio_interface(json_filepath):
    """ Gradio 处理函数，接收 JSON 文件路径，返回 DataFrame 和 CSV 下载路径 """
    df_results, output_csv_path = process_json_file(json_filepath)
    return df_results, output_csv_path

# 创建 Gradio 界面
with gr.Blocks() as demo:
    gr.Markdown("# JSON 分词统计工具")
    
    with gr.Row():
        json_input = gr.File(label="上传 JSON 文件", type="filepath")  # 修正 type 为 "filepath"
        process_button = gr.Button("处理文件")
    
    output_table = gr.Dataframe(label="分词统计结果")
    download_link = gr.File(label="下载 CSV 结果", type="filepath")  # 让 CSV 结果可以下载

    process_button.click(gradio_interface, inputs=[json_input], outputs=[output_table, download_link])

# 启动 Gradio 服务器，指定端口 10010
if __name__ == "__main__":
    demo.launch(server_port=10010)
