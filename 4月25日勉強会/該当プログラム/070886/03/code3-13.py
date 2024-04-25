birds = ["鳩","雀","オウム","フクロウ","ペンギン","鳩","オウム","雀"
         ,"カモメ","カラス","雀","鳩"]


birds_counter = dict()
for bird in birds:
    # birds_counter[bird] += 1
    if bird in birds_counter.keys():
        birds_counter[bird] += 1
    else:
        birds_counter[bird] = 1

for (k, v) in birds_counter.items():
    print(k + ": " + str(v))

from collections import defaultdict


birds_counter = defaultdict(int)

for bird in birds:
    birds_counter[bird] += 1

for k, v in birds_counter.items():
    print(f"{k}: {v}")