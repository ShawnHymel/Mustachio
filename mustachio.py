from SimpleCV import Camera, Image, HaarCascade

# Initialize camera
cam = Camera()

# Load the cascades
face_cascade = HaarCascade("/home/sgmustadio/mustachio/face.xml")
nose_cascade = HaarCascade("/home/sgmustadio/mustachio/nose.xml")
stache = Image("stache.png")
mask = stache.createAlphaMask()
mask = mask.invert()

# Capture image and find face
print "Cheese!"
img = cam.getImage()
img = img.scale(0.5)
faces = img.findHaarFeatures(face_cascade)

# Plaster on a 'stache
if ( faces is not None ) :
	print "Face found! Adding mustache"
	faces = faces.sortArea()
	face = faces[-1]
	myFace = face.crop()
	noses = myFace.findHaarFeatures(nose_cascade)
	nose = noses[0]
	xf = face.x - (face.width() / 2)
	yf = face.y - (face.height() / 2)
	xm = nose.x - (nose.width() / 2)
	ym = nose.y - (nose.height() / 2)
	xmust = xf + xm - (stache.width / 2) + (nose.width() / 2)
	ymust = yf + ym + (2 * nose.height() / 3)
	img = img.blit(stache, pos=(xmust, ymust), mask = mask)
	img.scale(2)
	img.save("myNewStache.jpg")


