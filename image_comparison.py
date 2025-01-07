import cv2
import face_recognition


img = cv2.imread("Messi1.webp")
if img is None:
    print("Error: Unable to load the image 'Messi1.webp'")
else:

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Encode the face in the first image
    img_encoding = face_recognition.face_encodings(rgb_img)
    if len(img_encoding) == 0:
        print("Error: No face found in 'Messi1.webp'")
    else:
        img_encoding = img_encoding[0]


        img2 = cv2.imread("images/Messi.webp")
        if img2 is None:
            print("Error: Unable to load the image 'images/Messi.webp'")
        else:

            rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            # Encode the face in the second image
            img_encoding2 = face_recognition.face_encodings(rgb_img2)
            if len(img_encoding2) == 0:
                print("Error: No face found in 'images/Messi.webp'")
            else:
                img_encoding2 = img_encoding2[0]


                result = face_recognition.compare_faces([img_encoding], img_encoding2)
                print("Result: ", result)


                cv2.imshow("Img", img)
                cv2.imshow("Img 2", img2)


                cv2.waitKey(0)
                # Close all windows
                cv2.destroyAllWindows()