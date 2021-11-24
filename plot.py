import json
from collections import Counter
import pickle

with open("data/pp_authors.txt", "rb") as fp:  # Unpickling
    pp_authors = pickle.load(fp)

unis = json.load(open("data/alias_map.json"))
affi_count = Counter()

new = []
for pp in pp_authors:
    list_aff = []
    for author in pp:
        aff_full = author[author.find("(") + 1 : author.find("')")].lower()
        for aff_nml in unis:
            if aff_full in unis[aff_nml] and aff_nml not in list_aff:
                list_aff.append(aff_nml)

    for aff in list_aff:
        affi_count[aff] += 1

academic_prefix = [
    "university",
    "univerisity",
    "institute",
    "uc ",
    "mit",
    "college",
    "telecom paris",
    "chinese academy of sciences",
    "school",
    "lawrence livermore national laboratory",
    "kaist",
    "kaust",
    "ist austria",
    "cnrs",
    "universit\u00e9",
    "irit",
    "inria",
    "college",
    "mila",
    "eth zurich",
    "oxford",
    "cornell",
    "harvard",
    "csiro",
    "tu darmstadt",
    "kth",
    "virginia tech",
    "\u00e9cole polytechnique f\u00e9d\u00e9rale de lausanne",
    "ens",
    "academy",
    "unist",
    "national",
    "yale",
    "universite",
    "universidad",
    "univ.",
    "lmu munich",
    "cuny",
    "tu dresden",
    "technion",
    "postech",
    "telecom sudparis",
]


def is_academic(affi):
    for prefix in academic_prefix:
        if prefix in affi:
            return True
    return False


academic_affi_count = Counter({k: v for k, v in dict(affi_count).items() if is_academic(k)})
industry_affi_count = Counter({k: v for k, v in dict(affi_count).items() if not is_academic(k)})

affi_count = sorted(affi_count.items(), key=lambda x: x[1], reverse=True)
# Serializing json
json_object = json.dumps(affi_count, indent=4, sort_keys=True)

# Writing to sample.json
with open("out.json", "w") as outfile:
    outfile.write(json_object)
