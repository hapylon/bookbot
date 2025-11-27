def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

def word_count(filepath):
    text = get_book_text(filepath)
    word_set = text.split()
    print(f"Found {len(word_set)} total words")

def char_counts(filepath):
    text = get_book_text(filepath).lower()
    counts = {}
    for i in text:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def sort_on(items):
    return items["num"]

def char_dicts(filepath):
    raw = char_counts(filepath)
    processed = []
    for key, value in raw.items():
        if key.isalpha() == False:
            continue
        packet = {"char": key, "num": value}
        processed.append(packet)
    processed.sort(reverse=True, key=sort_on)
    return processed
