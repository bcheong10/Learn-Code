import cv2 as cv
import os

def extraction(DIR, SAVE, FPS):
    fps = 0

    for i in os.listdir(DIR):

        count = 1
        save_path = os.path.join(SAVE, i[:-4])
        os.mkdir(save_path)
        path = os.path.join(DIR, i)
        video = cv.VideoCapture(path)
        
        while video.isOpened():
            ret, frame = video.read()

            if ret:
                cv.imwrite(os.path.join(save_path, f'frame{count}.jpg'), frame)
                add_frame = 30/FPS
                fps += int(add_frame)
                video.set(cv.CAP_PROP_POS_FRAMES, fps)
                print(f"Extracting frame: {count}")
                count += 1

            else:
                video.release()
                break

    print("Extraction complete!")


if __name__ == "__main__":

    # Directory containing raw videos
    DIR = r"C:\Users\bcheo\Desktop\14_10_2022_RGB"

    # Directory to save frames in
    SAVE = r"C:\Users\bcheo\Desktop\New_folder"

    # No. of frames to extract per second
    FPS = 5

    extraction(DIR, SAVE, FPS)


