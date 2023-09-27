import cv2, os

def flip_images():
	gest_folder = "D:/SNU/Github/Programming-in-Python/PIP_Mine_2/gestures2"
	images_labels = []
	images = []
	labels = []
	for g_id in os.listdir(gest_folder):
		#g_id=str(0)
		for i in range(2400):
			path = gest_folder+"/"+g_id+"/"+str(i+1)+".jpg"
			#new_path = gest_folder+"/"+g_id+"/"+str(i+1+1200)+".jpg"
			print(path)
			img = cv2.imread(path, 0)
			img = cv2.flip(img, 1)
			cv2.imwrite(path, img)

flip_images()
