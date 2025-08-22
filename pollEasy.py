import time
import openai
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ========= config area =========
GPT_MODEL = "gpt-4o"  # you could modifiy your own models
ANSWER_URL = "https://pollev.com/XXX"  # your pollev link
OPENAI_API_KEY = "skiXXXXXXX"  # remember to replace the example api_key to yours
# ===============================

openai.api_key = OPENAI_API_KEY

# set up chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # don't close the window while finished the task
driver = webdriver.Chrome(options=chrome_options)

# login
print("🔵 Please login Polleverywhere mannually and move to quiz page：")
print(f"👉 {ANSWER_URL}")
input("🟢 after you finished login, please press 'ENTER' to continue")

driver.get(ANSWER_URL)
time.sleep(2)

last_question_text = None

def wait_for_question_and_options(timeout=20):
    print("⌛ waiting for the question and choices to be loaded...")
    start = time.time()
    while time.time() - start < timeout:
        try:
            question_el = driver.find_element(By.TAG_NAME, "h1")
            buttons = driver.find_elements(By.CLASS_NAME, "component-response-multiple-choice__option__vote")
            if question_el and buttons:
                print("✅ question and choices are being loaded")
                return question_el, buttons
        except:
            pass
        time.sleep(0.5)
    return None, []

def get_option_texts(buttons):
    texts = []
    for btn in buttons:
        try:
            val = btn.find_element(By.CLASS_NAME, "component-response-multiple-choice__option__value")
            texts.append(val.text.strip())
        except:
            texts.append("<empty>")
    return texts

def is_already_answered(buttons):
    for btn in buttons:
        class_attr = btn.get_attribute("class")
        if "selected" in class_attr or "disabled" in class_attr:
            return True
    return False

def ask_gpt_letter(question, options):
    prompt = f"""
You are an expert in quiz challenges. Based on the question and choices given to you , you need to think step by step and judge for the only answer, which is the most possible and resonable one.
After finding out the answer, you must only reply one capitalized English character（for example A、B、C、D). Do not reply any other texts.

question：{question}

choices：
"""
    for idx, opt in enumerate(options):
        prompt += f"{chr(65 + idx)}. {opt}\n"

    response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message.content.strip().upper()
    print(f"🤖 ChatGPT replied：{reply}")
    return reply

try:
    while True:
        question_el, buttons = wait_for_question_and_options()
        if not question_el or not buttons:
            print("🕐 no questions at this time, wait for next round check...")
            time.sleep(5)
            continue

        question_text = question_el.text.strip()
        options = get_option_texts(buttons)

        print(f"📘 question：{question_text}")
        print(f"🔘 choices：{options}")

        if question_text == last_question_text:
            print("⏩ the question has not changed, wait for next round check")
            time.sleep(5)
            continue

        if is_already_answered(buttons):
            print("🟡 the question is being answerd, wait for next question...")
            last_question_text = question_text
            time.sleep(5)
            continue

        answer_letter = ask_gpt_letter(question_text, options)
        if len(answer_letter) == 1 and "A" <= answer_letter <= chr(65 + len(buttons) - 1):
            index = ord(answer_letter) - ord("A")
            buttons[index].click()
            print(f"✅ has clicked the choice {answer_letter}：{options[index]}")
            last_question_text = question_text
        else:
            print("⚠️ reply from chatGPT is invalid or out of range, jump")

        time.sleep(5)

except KeyboardInterrupt:
    print("🛑 the program is being terminated manually")
    driver.quit()
