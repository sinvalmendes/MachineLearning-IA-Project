from SimpleCV import *
hhfe = HueHistogramFeatureExtractor(20)
ehfe = EdgeHistogramFeatureExtractor(20)
#haarlike = HaarLikeFeatureExtractor(fname="../../../SimpleCV/SimpleCV/Features/haar.txt")
extractors = [hhfe,ehfe]#,haarlike]
svm = SVMClassifier(extractors)
tree = TreeClassifier(extractors)
trainPaths = ['./branca', './negra']
testPaths = ['./branca-test/', './negra-test/']
classes = ['branca', 'negra']



print svm.train(trainPaths, classes, verbose=True)
print tree.train(trainPaths, classes, verbose=True)
#print svm.test(testPaths, classes, verbose=True)
#print tree.test(testPaths, classes, verbose=True)

count = 1
testImageSet = ImageSet()
for p in testPaths:
	testImageSet += ImageSet(p)

for t in testImageSet:
	className = svm.classify(t)
	t.drawText(className,10,10,fontsize=80,color=Color.YELLOW)
	fname = "./results/classification"+str(count)+".png"
	t.applyLayers().save(fname)
	count+=1
