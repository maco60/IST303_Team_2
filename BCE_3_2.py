#Task 1 Answer:
beatles = [('George', 'guitar'), ('John', 'guitar'), ('Paul', 'bass'), ('Ringo', 'drums')]

#Task 2 Answer:
beatles_dict = dict()
for bn, bi in beatles:
    beatles_dict[bn] = bi

#Task 3 Answer:
stones = [('Mick', 'piano'), ('Keith', 'guitar'), ('Charlie', 'drums'), ('Ronnie', 'guitar')]

#Task 4 Answer:
stones_dict = dict()
for sn, si in stones:
    stones_dict[sn] = si

#Task 5 Answer:
bands_dict = dict()
bands_dict['Beatles'] = beatles_dict
bands_dict['Stones'] = stones_dict

#Task 6 Answer:
print(bands_dict['Beatles']['Ringo'])
