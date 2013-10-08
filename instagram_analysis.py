from instagram.client import InstagramAPI
from SimpleCV import Image
import time
from ethnicity import *

def getInstagramMediaUrl(media):
        return media.images['standard_resolution'].url

def getInstagramImage(media):
        imageUrl = getInstagramMediaUrl(media)
        image = Image(imageUrl)
        return image

def showInstagramImage(media):
        image = getInstagramImage(media)
        image.show()


def setMediaValues(media, className):
        mediaValues = {}
        mediaValues.setdefault("url",getInstagramMediaUrl(media))
        mediaValues.setdefault("etnia",className)
        mediaValues.setdefault("longitude", media.location.point.longitude)
        mediaValues.setdefault("latitude", media.location.point.latitude)
        return mediaValues
        
api = InstagramAPI(client_id="b8bdb129b9984e8cad04af04343257ca",
                   client_secret="e311b1d04143418d86b152db848205d7")
tag = "face" #"selfie"

resultTuple = api.tag_recent_media(0, 10, tag)
#locationMedias = api.media_search(100,100,-7.131724,-34.82254,1,5000000000000)

medias = resultTuple[0]
addr = resultTuple[1]
count = 1
mediaNode = {}
mediasJson = {}
for media in medias:
	showInstagramImage(media)
	if hasattr(media, 'location'):
		image = getInstagramImage(media)
		haarCascades = ["face"]
		for haarCascade in haarCascades:
			img = image.flipHorizontal()
			features = img.findHaarFeatures(haarCascade)
			if features:
				for feature in features:
					cropFeature = feature.crop()
					className = classifyEthnicity(cropFeature)
					cropFeature.drawText(className,10,10,fontsize=30,color=Color.YELLOW)
					cropFeature.show()
					mediaNode = {}
					mediaValues = setMediaValues(media, className)
					mediasJson.setdefault("%d.jpg"%count,mediaValues)
					cropFeature.save('%d.jpg'%count)
					count += 1
with open('data.txt', 'w') as outfile:
        json.dump(mediasJson, outfile)
	
