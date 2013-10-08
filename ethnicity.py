from SimpleCV import *

hhfe = HueHistogramFeatureExtractor(100)
ehfe = EdgeHistogramFeatureExtractor(20)

extractors = [hhfe,ehfe]
knn = KNNClassifier(extractors,6, None)
svm = SVMClassifier(extractors)
tree = TreeClassifier(extractors)
naive = NaiveBayesClassifier(extractors)

trainPaths = ['./branca', './negra']
#testPaths = ['./tests/']
classes = ['W', 'B']

#print svm.train(trainPaths, classes, verbose=True)
#print tree.train(trainPaths, classes, verbose=True)
#print naive.train(trainPaths, classes, verbose=False)
print knn.train(trainPaths, classes, verbose=False)

def classifyEthnicity(img):
        className = knn.classify(img)
        return className

#count = 1
#testImageSet = ImageSet()
#for p in testPaths:
#	testImageSet += ImageSet(p)

#for t in testImageSet:
#	className = knn.classify(t)
#	t.drawText(className,10,10,fontsize=30,color=Color.YELLOW)
#	fname = "./results/classification"+str(count)+".png"
#	t.applyLayers().save(fname)
#	count+=1

