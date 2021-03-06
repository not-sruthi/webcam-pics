import time
import cv2
import dropbox


startTime = time.time()

#to take pictures from webcam and saving them
def takePic(n):
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite('pic' + str(n) +'.jpg', frame)
        img = 'pic' + str(n) +'.jpg'
        result = False

    videoCaptureObject.release()
    cv2.destroyAllWindows
    return(img)

#to upload pictures to dropbox
def uploadPic(img):
    accessToken= 'alJYiWd_lRYAAAAAAAAAATCaNHtOfk6FzZVQUgSQceeqe133912Dt5mbUHXrEFf4'
    file= img
    fileFrom= file
    fileTo= '/webcamPics/' + (img)
    db = dropbox.Dropbox(accessToken)

    with open (fileFrom, 'rb') as f:
        db.files_upload(f.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
        print('success')

#taking pictures at 5 second intervals and uploading them to dropbox
def main():
    isRunning = True   
    no = 0

    while (isRunning) :
        if ((time.time() - startTime) >= 5):
            no = no + 1
            name = takePic(no)
            uploadPic(name)

main()
