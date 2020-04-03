#! python3
# autoForm.py - automatically fill the form

import pyautogui, time

formData = [{'name': 'aaaa', 'fear': 'bbbb', 'source': 'wand', 'robocop':4, 'comments':'Tell Bob I said Hi'},{'name': 'aaaa', 'fear': 'bbbb', 'source': 'wand', 'robocop':4, 'comments':'Tell Bob I said Hi'},{'name': 'aaaa', 'fear': 'bbbb', 'source': 'wand', 'robocop':4, 'comments':'Tell Bob I said Hi'},{'name': 'aaaa', 'fear': 'bbbb', 'source': 'wand', 'robocop':4, 'comments':'Tell Bob I said Hi'},]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded')

for person in formData:
  print('>>>5 sec pause for ctrl-C <<<')
  time.sleep(5)
  print('Entering Name')
  pyautogui.write(['\t','\t'])
  pyautogui.write(person['name'] + '\t')
  pyautogui.write(person['fear'] + '\t')
  if person['source'] == 'wand':
    pyautogui.write(['down','enter', '\t'], 0.5)
  if person['robocop'] == 4:
    pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
  pyautogui.write(person['comments'] + '\t')
  time.sleep(0.5)
  pyautogui.press('enter')

  print('Submitted')
  time.sleep(5)
  pyautogui.write(['\t', 'enter'], 0.5)

