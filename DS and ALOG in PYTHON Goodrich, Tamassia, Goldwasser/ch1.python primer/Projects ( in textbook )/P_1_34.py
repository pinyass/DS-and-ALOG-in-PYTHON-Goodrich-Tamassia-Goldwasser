import random

sentences = [ "I will never spam my friends again.",
              "I well never spam my friends again.",
              "I will nevar spam my friends again.",
              "I will never span my friends again.",
              "I will never spam ny friends again.",
              "I will never spam my friands again.",
              "I will never spam my friends agein.",
              "I will never spam my friends agaim."]

for i in range(100):
    index = random.randint(0,7)
    print(sentences[index])
