如何使用此程式碼庫翻譯 SRT 字幕文件：


此程式碼庫旨在翻譯 .srt 字幕文件，同時保留原始字幕。


系統需求: Windows 或 Mac。
安裝:

1.
複製儲存庫：git clone https://github.com/elbartohub/Bilingual-SRT

3.
安裝必要套件：pip install -r requirements.txt
執行方式:


若要翻譯字幕並保留原始字幕，請使用以下指令： python srt_translate.py input.srt 這會將英文字幕翻譯成中文，並同時顯示英文和中文。



若要指定原始語言和目標語言，並同時保留原始字幕，請使用以下指令： python srt_translate.py input.srt en zh-TW both
參數說明:



<input_file>：要翻譯的字幕文件的路徑（必需）。



[source_lang]：原始語言代碼（可選，預設為 en）。



[target_lang]：目標語言代碼（可選，預設為 zh-TW）。


範例:


若要將名為 subtitle.srt 的英文字幕文件翻譯成繁體中文，並將翻譯後的字幕儲存到 subtitle_zh-TW.srt，請使用以下指令：


python srt_translate.py subtitle.srt en zh-TW both


這會在 subtitle_zh-TW.srt 中產生一個新的字幕文件，其中包含英文和繁體中文的雙語字幕。


程式碼說明:



程式碼使用 translate 套件進行翻譯。



程式碼使用 tqdm 套件顯示翻譯進度。



程式碼會檢查每一行是否為字幕文本行，並僅翻譯字幕文本行。



如果翻譯失敗，程式碼會保留原始字幕。
請注意，您需要安裝 translate 和 tqdm 套件才能執行此程式碼。您可以使用 pip install translate tqdm 指令安裝這些套件。

執行結果：

![image](https://github.com/user-attachments/assets/264252b8-957b-4c92-924a-a433d29d3fcb)

