import cv2


class Camera:
    def __init__(self, cam_preset_num=5):
        self.cam_preset_num = cam_preset_num

    def get_cam_num(self):
        cnt = 0
        devices = []  # 初始化一个空列表，用来存储可用的设备编号
        for device in range(0, self.cam_preset_num):  # 循环遍历设备编号，范围为0到self.cam_preset_num-1
            stream = cv2.VideoCapture(device, cv2.CAP_DSHOW)  # 根据设备编号实例化一个视频流对象
            grabbed = stream.grab()  # 尝试从该设备获取一帧图像
            stream.release()  # 释放视频流对象
            if not grabbed:  # 如果无法获取到图像，则说明该设备不可用
                continue  # 循环继续，跳过本次循环
            else:  # 如果能够获取到图像，则说明该设备可用
                cnt = cnt + 1  # 对可用设备计数器进行自增
                devices.append(device)  # 将可用设备的编号添加到devices列表中
        return cnt, devices  # 返回可用设备数量和设备列表


if __name__ == '__main__':
    cam = Camera()
    cam_num, devices = cam.get_cam_num()
    print(cam_num, devices)
