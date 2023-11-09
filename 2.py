
# python train.py --name tea2_rgba_c2d_depth  --data data/tea2_4h/rgba_c2d_depth.yaml --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py  --data data/tea2_4h/rgba_c2d_depth.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\tea2_rgba_c2d_depth\weights\best.pt --device 0

# python train.py --name tea2_rgba_c2d_ir  --data data/tea2_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 0;
# python test.py  --data data/tea2_4h/rgba_c2d_ir.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\tea2_rgba_c2d_ir\weights\best.pt --device 0

# python train.py --name tea2_rgba_c2d_depth_ir --data data/tea2_4h/rgba_c2d_depth_ir.yaml --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 1;
# python test.py  --data data/tea2_4h/rgba_c2d_depth_ir.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\tea2_rgba_c2d_depth_ir3\weights\best.pt --device 0


# python train.py --name tea2_rgba_c2d_depth  --data data/tea2_4h/rgba_c2d_depth.yaml --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 1; python train.py --name tea2_rgba_c2d_ir  --data data/tea2_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 1; python train.py --name tea2_rgba_c2d_depth_ir --data data/tea2_4h/rgba_c2d_depth_ir.yaml --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 1;
