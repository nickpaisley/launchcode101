def analyze_text(text):
    filtered = [t.lower() for t in text if t.isalpha()]
    cnt = filtered.count('e')
    result = "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(len(filtered),cnt,str(100*cnt/len(filtered)) [:13])
    return result
