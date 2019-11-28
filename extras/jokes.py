import pyjokes

with open('./myJoke.txt', 'w') as f:
  f.write(pyjokes.get_joke())