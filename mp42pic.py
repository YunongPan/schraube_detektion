#!/usr/bin/env python

import cv2
import os
import shutil
 
def get_frame_from_video(video_name, interval):
####
 
    #################
    save_path = video_name.split('.mp4')[0] + '/'
    is_exists = os.path.exists(save_path)
    if not is_exists:
        os.makedirs(save_path)
        print('path of %s is build' % save_path)
    else:
        shutil.rmtree(save_path)
        os.makedirs(save_path)
        print('path of %s already exist and rebuild' % save_path)
 
    ###############
    video_capture = cv2.VideoCapture(video_name)
    i = 0
    j = 0
 
    while True:
        success, frame = video_capture.read()
        i += 1
        if i % interval == 0:
            #################
            j += 1
            save_name = save_path + str(j) + '_' + str(i) + '.jpg'
            cv2.imwrite(save_name, frame)
            print('image of %s is saved' % save_name)
        if not success:
            print('video is all read')
            break
 
 
if __name__ == '__main__':
    ##################
    video_name = './VID_20210507_092322.mp4'
    interval = 50
    get_frame_from_video(video_name, interval)
