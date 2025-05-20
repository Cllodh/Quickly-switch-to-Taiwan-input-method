from flask import Flask, render_template, request, jsonify
from pypinyin import pinyin, Style, BOPOMOFO

app = Flask(__name__)

# Windows 注音輸入法對照表
BOPOMOFO_MAP = {
    'ㄅ': '1', 'ㄆ': 'q', 'ㄇ': 'a', 'ㄈ': 'z',
    'ㄉ': '2', 'ㄊ': 'w', 'ㄋ': 's', 'ㄌ': 'x',
    'ㄍ': 'e', 'ㄎ': 'd', 'ㄏ': 'c',
    'ㄐ': 'r', 'ㄑ': 'f', 'ㄒ': 'v',
    'ㄓ': '5', 'ㄔ': 't', 'ㄕ': 'g', 'ㄖ': 'b',
    'ㄗ': 'y', 'ㄘ': 'h', 'ㄙ': 'n',
    'ㄧ': 'u', 'ㄨ': 'j', 'ㄩ': 'm',
    'ㄚ': '8', 'ㄛ': 'i', 'ㄜ': 'k', 'ㄝ': ',',
    'ㄞ': '9', 'ㄟ': 'o', 'ㄠ': 'l', 'ㄡ': '.',
    'ㄢ': '0', 'ㄣ': 'p', 'ㄤ': ';', 'ㄥ': '/',
    'ㄦ': '-',
    'ˊ': '6', 'ˇ': '3', 'ˋ': '4', '˙': '7'
}

def convert_to_bopomofo(text):
    # 使用 pypinyin 將中文字轉換為注音符號
    bopomofo_list = pinyin(text, style=BOPOMOFO)
    bopomofo_result = ''
    key_result = ''
    
    for bopomofo in bopomofo_list:
        if bopomofo[0]:  # 確保注音不為空
            # 保存注音符號
            bopomofo_result += bopomofo[0] + ' '
            
            # 轉換為鍵盤按鍵
            for char in bopomofo[0]:
                if char in BOPOMOFO_MAP:
                    key_result += BOPOMOFO_MAP[char]
                else:
                    key_result += char
            key_result += ' '
    
    return bopomofo_result.strip(), key_result.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.json.get('text', '')
    bopomofo, keys = convert_to_bopomofo(text)
    return jsonify({
        'bopomofo': bopomofo,
        'result': keys
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 