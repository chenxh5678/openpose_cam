import sys
import cv2
import os

def analys():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(dir_path + '/pyopen')
    os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64;' +  dir_path + '/bin;'
    import pyopenpose as op

    # 载入模型文件
    params = dict()
    params["model_folder"] = "models/"
    # 启动OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    datum = op.Datum()
    cap = cv2.VideoCapture(1)  # 读取摄像头或视频
    while cap.isOpened():
        ret,fram = cap.read()
        if ret == True:
            datum.cvInputData = fram
            opWrapper.emplaceAndPop(op.VectorDatum([datum]))
            # data = datum.poseKeypoints  # 关键点列表数组
            cv2.imshow('Press Q to exit',datum.cvOutputData)
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    analys()
    