def bpe(txt):
    voc = vocabulary_words(txt)
    voc_chars = vocabulary_chars(txt)
    paired_chars = pairs(voc)
    paired_chars_list = sorted(paired_chars.items(), key=lambda x: x[1], reverse=True)
    for elem in paired_chars_list:
        voc_chars[elem[0]] = elem[1]
    print(len(voc_chars))
    return voc_chars

def vocabulary_words(txt):
    voc_dct = dict()
    for elem in txt:
        if elem not in voc_dct.keys():
            voc_dct[elem] = txt.count(elem)
    return voc_dct

def vocabulary_chars(txt):
    voc_dct = dict()
    txt = ''.join(txt)
    for elem in txt:
        if elem not in voc_dct.keys():
            voc_dct[elem] = txt.count(elem)
    return voc_dct

def pairs(voc):
    p = dict()
    for elem in voc.items():
        chars = [*elem[0]]
        for i in range(len(chars) - 1):
            pair = chars[i] + chars[i + 1]
            freq = elem[0].count(pair) * elem[1]
            if pair in p.keys():
                p[pair] += freq
            else:
                p[pair] = freq
    return p

text = '''In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that 
means comfort. 
It had a perfectly round door like a porthole, painted green, with a shiny yellow brass knob in the exact middle. The door opened on to a tube-shaped hall like a tunnel: a very comfortable tunnel without smoke, with panelled walls, and floors tiled and carpeted, provided with polished chairs, and lots and lots of pegs for hats and coats - the hobbit was fond of visitors. The tunnel wound on and on, going fairly but not quite straight into the side of the hill - The Hill, as all the people for many miles round called it - and many little round doors opened out of it, first on one side and then on another. 
No going upstairs for the hobbit: bedrooms, bathrooms, cellars, pantries (lots of these), wardrobes (he had whole 
rooms devoted to clothes), kitchens, dining-rooms, all were on the same floor, and indeed on the same passage. 
The best rooms were all on the lefthand side (going in), for these were the only ones to have windows, deep-set round windows looking over his garden, and meadows beyond, sloping down to the river.'''

text = str.lower(text)
text = text.replace('\n', '')
text = text.split(' ')
bpe_pairs = bpe(text)
print(bpe_pairs)
