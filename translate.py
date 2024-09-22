import re
import sys
from translate import Translator
from tqdm import tqdm

def translate_srt(input_file, output_file, source_lang="en", target_lang="zh-TW", keep_original=False):
    translator = Translator(to_lang=target_lang, from_lang=source_lang)

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
                if keep_original:
                    translated_content.append(line)  # 添加原始字幕
                translated_content.append(translated_line + '\n')  # 添加翻譯
            except Exception as e:
                print(f"翻譯錯誤: {e}")
                translated_content.append(line)  # 當翻譯失敗，保留原始字幕

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_content)

# 從命令行獲取輸入和輸出文件
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 5:
        print("用法: python translate_srt.py <input_file> [source_lang] [target_lang] [both]")
        sys.exit(1)

    input_file = sys.argv[1]
    
    # 默認語言
    source_lang = "en"
    target_lang = "zh-TW"
    
    # 檢查是否提供了語言代碼和選項
    keep_original = False
    if len(sys.argv) > 2:
        source_lang = sys.argv[2]
        if len(sys.argv) > 3:
            target_lang = sys.argv[3]
        if len(sys.argv) == 5 and sys.argv[4].lower() == "both":
            keep_original = True

    # 自動生成輸出文件名並附加語言代碼
    output_file = input_file[:-4] + f'_{target_lang}.srt' if input_file.endswith('.srt') else input_file + f'_{target_lang}.srt'
    
    translate_srt(input_file, output_file, source_lang, target_lang, keep_original)