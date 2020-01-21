import re


def to_camel_case(text):
    return "".join(w if i == 0 else w.capitalize()
                   for i, w in enumerate(re.split("_|-", text)))
