# ������ҵĿ�Դ pyside6 + yolov5+active-learning��Ŀ����ӭ star![395494A6.png](https://cdn.nlark.com/yuque/0/2024/png/34454554/1714980244561-4f46267d-25f0-4a03-9b8a-2bf4de7d3b58.png#averageHue=%2354472a&clientId=u04ab15bb-705b-4&from=paste&height=48&id=u2733e641&originHeight=48&originWidth=48&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2823&status=done&style=none&taskId=u243c43ab-fa0c-4a3d-99b2-db8ba5a2e5f&title=&width=48) and follow!

# ��Ŀ����

�Ұ�һЩ�ļ���ɾ���� ����segement ʲô�� <br />������ԭ����yolov5 7.0���°�װ<br />����Ҫ�ľ��������ļ�<br />�ֱ���ui.py
MainQt.py<br />ֱ������MainQt.py����<br />����Ҫ��pt�ļ�����data/models/biology.pt<br />
������yolov5���+����ѧϰ�ܳ���������Ѫϸ����ģ��<br />Ŀǰ����0.8 ���Ƚϸ�<br />����֧���л�ģ�� �л���ԭ����yolov5m.pt
֧�ֶ�����Ŀ�����ʶ��<br />![](https://github.com/huange888/yolov5_7.0_pyside6_active_learning/assets/118048444/165a5c67-7a64-4cd3-8ed2-0292cab780e9#id=UtZd0&originHeight=823&originWidth=1376&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

# ���л���

```python
pip
install - r
requirements.txt
```

# ���з���

```python
python
MainQt.py
```

# ��Ŀ��ͼ

![](https://github.com/huange888/yolov5_7.0_pyside6_active_learning/assets/118048444/2cbce1b7-c8b5-4495-9183-bd05800b9d43#id=DI5yH&originHeight=823&originWidth=1376&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

# ���н���

����Ŀ��ʹ��PySide6�⿪����һ������YOLOv5��ͼ��ʶ��Ӧ�ó���<br />
�û�����ͨ����Ӧ�ó���ѡ��ͼ���ļ�������ͷʵʱ���Ŀ�����壬����ʾ�������<br />
ͬʱ����Ӧ�ó���֧������ѧϰ���ܣ��û������ֶ����һЩ����ļ�������԰���ģ�ͽ����Ż���<br />����Ŀǰ����ͷ��û������
ֻ��ʶ��ͼƬ ͬʱ������Ƶʶ�������ԭ��������м�� ��qt��ʵ�����н���  <br />��δ����ʵ����Ƶʶ��ģ��

# ��Ŀ�ṹ

# ������

## ������ť (Start Button)

- **��ť����**: `start_button`
- **����**: ��������ĳ�����̻����

## ͼƬ�ϴ���ť (Upload Image Button)

- **��ť����**: `upload_image_button`
- **����**: �����û��ϴ�ͼƬ�ļ���

## ģ���ϴ���ť (Upload PT Button)

- **��ť����**: `upload_pt_button`
- **����**: �����ϴ�ģ���ļ���ͨ��ָ����PyTorchģ���ļ���

## ���б�ǩ��ť (Label Run Button)

- **��ť����**: `Labelrun_button`
- **����**: ��������һ����ǻ������̡�

## ����ѧϰ���а�ť (Active Run Button)

- **��ť����**: `activeRun_button`
- **����**: ���ڼ����ʼһ��ʵʱ���еĹ��̡�

## ����ѧϰѵ����ť (Active Train Button)

- **��ť����**: `activeTrain_button`
- **����**: ��������ģ�͵Ļ�Ծѵ���׶Ρ�

## ����ģ�Ͱ�ť (Export Button)

- **��ť����**: `export_button`
- **����**: ���ڵ������ݻ�ģ�͵��ļ���

## ֹͣ���̰�ť (Stop Button)

- **��ť����**: `stop_button`
- **����**: ����ֹͣ��ǰ���еĹ��̡�

## �رմ��ڰ�ť (Close Button)

- **��ť����**: `close_button`
- **����**: ���ڹر�Ӧ�ó����ǰ���ڡ�
