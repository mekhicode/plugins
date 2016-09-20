# -*-coding: utf-8 -*-

# 摩斯代码表
CODE_TABLE = {
    # 26 个英文字符
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    # 10 个数字
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    # 16 个特殊字符
    ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
    '?': '..--..', '=': '-...-',  "'": '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
    ')': '-.--.-', '$': '...-..-','&': '. . . .','@': '.--.-.'

    # 你还可以自定义

}

def encode(msg):
    morse = ''
    for char in msg:
        if char == ' ':
            morse += ' '
        else:
            morse += CODE_TABLE[char.upper()] + ' '
    return morse

def decode(morse):
    msg = ''
    codes = morse.split(' ')

    for code in codes:
        if code == '':
            msg += ' '
        else:
            UNCODE = dict(map(lambda t: (t[1], t[0]), CODE_TABLE.items()))
            msg += UNCODE[code]

    return msg


def main():

    msg = "Hello World!"
    print msg

    morse = encode(msg)
    print morse

    string = decode(morse)
    print string

if __name__ == '__main__':
    main()