def designerPDFViewer(h, word):
	return (max(map(lambda c: h[ord(c)-96-1], word)) * len(word))

print(designerPDFViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5], 'tarn'))
