import pickle
import json

with open("pp_authors.txt", "rb") as fp:  # Unpickling
    pp_authors = pickle.load(fp)

unis = json.load(open("convert.json"))

new = []
for pp in pp_authors:
    for author in pp:
        aff_full = author[author.find("(") + 1 : author.find("')")].lower()
        is_in = False
        if aff_full in unis.keys():
            aff_name = unis[aff_full]
            is_in = True

        for x in unis:
            if unis[x] == aff_full:
                is_in = True

        if is_in == False:
            print(aff_full)
            if aff_full not in new:
                new.append(aff_full)
new.sort()
print(len(new))

obj = {}
for aff in new:
    obj[aff] = "to replace"

# Serializing json
json_object = json.dumps(obj, indent=4, sort_keys=True)

# Writing to sample.json
with open("to_convert.json", "w") as outfile:
    outfile.write(json_object)
