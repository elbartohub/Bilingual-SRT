import re
import sys
from translate import Translator
from tqdm import tqdm

def translate_srt(input_file, output_file):
    translator = Translator(to_lang="zh-TW", from_lang="en")

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    translated_content = []
    total_lines = len(content)

    for line in tqdm(content, desc="翻譯進度", total=total_lines):
        # 檢查是否為字幕文本行
        if re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', line):
            translated_content.append(line)  # 保留時間戳和索引
        else:
            try:
                translated_line = translator.translate(line.strip())
                translated_content.append(line)  # 添加原始英文字幕
                translated_content.append(translated_line + '\n')  # 添加繁體中文翻譯
            except Exception as e:
                print(f"翻譯錯誤: {e}")
                translated_content.append(line)  # 如果翻譯失敗，保留原始字幕

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_content)

# 從命令行獲取輸入和輸出文件路徑
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python translate_srt.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    translate_srt(input_file, output_file)