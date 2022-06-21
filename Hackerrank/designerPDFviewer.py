def designerPdfViewer(h, word):
    idx_arr = []
    for w in word:
        x = w
        idx_w = ord(x) - 97
        idx_arr.append(idx_w)
        
    h_arr = []
    for idx in idx_arr:
        y = h[idx]
        h_arr.append(y)
        
    return len(word) * max(h_arr)