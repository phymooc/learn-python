#! python3
# mclip.py -- a multi-clipboard program

import pyperclip
import sys
TEXT = {'agree': 'Yes, I agree',
        'busy': 'sorry, I\'m busy', 'upsell': '''ssssssssssssss'''}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase]-copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'text for {keyphrase} copied')
else:
    print(f'there is no text for {keyphrase}')
