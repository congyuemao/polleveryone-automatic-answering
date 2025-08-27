# PollEasy 点易通

An automatic answering script, based on Python + Selenium + OPENAI API.

一个基于Python + Selenium + OPENAI API的自动答题脚本。

It automatically monitors PollEverywhere quizes, send question and options to an AI model (ChatGPT for example), and automatically click the most reasonable and possible answer based on AI replies.

该脚本可自动监听浏览器中PollEverywhere的题目，并自动发送题目和选项至AI接口（比如ChatGPT），并根据AI返回答案，自动点击最可能的答案。

## Installation & Usage 安装及使用方法

### 1. clone the respository 克隆仓库

   ```bash
    git clone https://github.com/congyuemao/polleveryone-automatic-answering.git
    cd polleveryone-automatic-answering
   ```

### 2. required packages 依赖包
   Make sure you have installed Python 3.8+ and Google Chrome. After that, install required packages.
   
   确保你已经安装 Python 3.8+ 以及谷歌Chrome浏览器。之后，安装依赖包。
   
    pip install openai selenium
   
### 3. configure the script 设置脚本参数

At the top of the `pollEasy.py` , modifiy the following values before use.

在使用该脚本前，请在 `pollEase.py` 顶部设置如下参数。

```
GPT_MODEL = "gpt-4o"                     # Choose your preferred AI model 选择你喜欢的AI模型
ANSWER_URL = "https://pollev.com/XXX"    # Your PollEverywhere quiz link 设置PollEverywhere答题链接
OPENAI_API_KEY = "sk-XXXX"               # Replace with your AI API key 将此处替换成为你自己的AI API key
```

###  4. Run the script 运行脚本

    python pollEasy.py
    
    
#### Steps:

1. Manually type in the link and login PollEverywhere in the opened Chrome window. 
   
   手动在打开的Chrome窗口中输入链接，登录PollEverywhere账号。
   
3. After you successfully logged in PollEverywhere and jumped to the answering window, please press ENTER in the terminal to continue.
   
   当界面停留在答题链接界面并成功登录后，在控制台中按下ENTER以继续。
   
5. The script will monitor questions, query AI for an answer, and automatically select the option.
   
   脚本会自动监听问题，并向AI询问，然后自动选择答案进行点击回答。

## Notes 注意事项

Please check your computer’s power settings and keep the screen on while the script is running. 

请注意电脑电源设置，在脚本运行期间保持屏幕开启。

If the screen turns off or the computer enters standby mode, the script will not function properly and may fail to capture and answer the questions.

如果息屏或者待机，脚本将无法正常工作，可能导致无法抓取题目作答。

## Disclaimer 免责声明

This project is for educational and personal learning purposes only.

此项目仅供教育以及个人学习用途。

Do not use it in violation of PollEverywhere’s terms of service or academic integrity rules.

请勿使用此项目进行违反PollEverywhere用户协议或有违学术诚信的活动。

Use at your own risk.

使用责任由用户自负。
