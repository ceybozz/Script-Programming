# h14ceybo
# Ceyhun Bozkurt

import cv2, numpy, os

# main method 
def main():
    def task():
        task = 0
        while task !=4:
            task = terminal_display()
            if task == 1:
                face_detect()
            if task == 2: 
                face_train()
            if task == 3:
                face_recognition()
            if task == 4:
                help()
            if task == 5:
                print('Program has ended!')
                quit()
    # Terminal display
    def terminal_display(): 
        print('\n#####################################################')
        print('              Face Recognition Program               ')
        print('#######################################################')
        print('1- Face detect and data gathering')
        print('2- Face training')
        print('3- Face recognition')
        print('4- Help')
        print('5- Quit') 
        print('#######################################################\n')
        task = int(input('Type 1-5: '))
        while task < 1 or task > 5:
            task = int(input('Choose between 1 - 5.\nOops! Plz try again: '))
        return task

    def face_train():
        models = ['Ben Afflek','2pac Shakur', 'Elton John']
        DIR = r'C:\Users\ceybo\Desktop\Labb6 h14ceybo\Faces\train' 
        haar_cascade = cv2.CascadeClassifier('haar_face.xml') 
        features = []
        labels = []

        def create_train():
            for person in models:
                path = os.path.join(DIR, person)
                label = models.index(person)

                for img in os.listdir(path):
                    img_path = os.path.join(path, img)
                    img_array = cv2.imread(img_path)
                    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
                    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 5)
                    
                    for (x,y,w,h) in faces_rect:
                        faces_roi = gray[y:y+h, x:x+w]
                        features.append(faces_roi)
                        labels.append(label)

        create_train()
        print('Collecting Training Data done ---------------------')

        features = numpy.array(features, 'object')
        labels = numpy.array(labels)

        face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        face_recognizer.train(features, labels) 
        face_recognizer.save('face_traine.yml')
        numpy.save('features.npy', features)
        numpy.save('label.npy', labels)

    def face_recognition():
        haar_cascade = cv2.CascadeClassifier('haar_face.xml')
        models1 = ['Ben Afflek','2pac Shakur', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('face_traine.yml')
        img = cv2.imread(r'Faces\val\2pac_shakur/3.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h,x:x+w]
            label, confidence = face_recognizer.predict(faces_roi)
            print(f'Label = {models1[label]} with a confidence of {confidence} %')
            cv2.putText(img, str(models1[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.imshow('Detected Face', img)
        cv2.waitKey(0)
    
    def face_detect():
        img = cv2.imread('Photos/group 4.jpg')
        haar_cascade = cv2.CascadeClassifier('haar_face.xml')
        faces_rect = haar_cascade.detectMultiScale(img, 1.1, 1) 
        print(f'Number of faces found = {len(faces_rect)}')
        for (x,y,w,h) in faces_rect:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.imshow('Detected Faces', img)
        cv2.waitKey(0)

    def help():
        print('OBS! Change path of "DIR" in the "def faceTraining" depending on where you save the folder.')
        print('-------------------------------------------------------------------------------------')
        print('By Pressing 1, this program can detect faces of a group people.')
        print('By Pressing 2, you register a face to "train" by pictures in folder.')
        print('By Pressing 3, you compare others pictures of the same person, \n And estimate the similarities in percentage.')
        print('By Pressing 5, Exit the program.')
    task()
# end of program, closeing the main method
main()