



# python train.py  --data data/voc_tea_rgba_depth.yaml --batch-size 2  --cfg models/yolov5s_tea.yaml   --device 1 --name ts2_buds_depth;
# python train.py  --data data/voc_tea_rgba_ir.yaml --batch-size 2  --cfg models/yolov5s_tea.yaml   --device 1 --name ts2_buds_ir;
# python test.py  --data data/voc_tea_rgba_depth.yaml --weights runs/train/ts2_buds_depth7/weights/best.pt
# python test.py  --data data/voc_tea_rgba_ir.yaml --weights runs/train/ts2_buds_ir/weights/best.pt

# models/yolov5s_ch4.yaml
# python train.py  --data data/voc_tea_rgba_depth.yaml --batch-size 2  --cfg models/yolov5s_ch4.yaml   --device 1 --name ts2_rgba_depth;
# python train.py  --data data/voc_tea_rgba_ir.yaml --batch-size 2  --cfg models/yolov5s_ch4.yaml   --device 1 --name ts2_rgba_ir;
# python test.py  --data data/voc_tea_rgba_depth.yaml --weights runs/train/ts2_rgba_depth/weights/best.pt
# python test.py  --data data/voc_tea_rgba_ir.yaml --weights runs/train/ts2_buds_ir2/weights/best.pt

# python test.py  --data data/voc_tea_rgba_depth.yaml --weights runs/train/ts2_rgba_depth_pre4/weights/best.pt
# python test.py  --data data/voc_tea_rgba_ir.yaml --weights runs/train/ts2_rgba_ir_pre3/weights/best.pt
# python test.py  --data data/voc_tea.yaml --weights runs/train/ts2_rgb_pre2/weights/best.pt

# python train.py  --data data/voc_tea_rgba_depth.yaml  --batch-size 2  --cfg models/yolov5s_ch4.yaml --epochs 1000  --device 0 --name ts2_rgba_depth_pre;
# python train.py  --data data/voc_tea_rgba_ir.yaml  --batch-size 2  --cfg models/yolov5s_ch4.yaml  --epochs 1000  --device 0 --name ts2_rgba_ir_pre;
# python train.py  --data data/voc_tea.yaml  --batch-size 2  --cfg models/yolov5s_new.yaml  --epochs 1000  --device 1 --name ts2_rgb_pre;
# python test.py  --data data/voc_tea_rgba_depth.yaml --weights runs/train/ts2_rgba_depth_pre5/weights/best.pt
# python test.py  --data data/voc_tea_rgba_ir.yaml --weights runs/train/ts2_rgba_ir_pre4/weights/best.pt
# python test.py  --data data/voc_tea.yaml --weights runs/train/ts2_rgb_pre3/weights/best.pt

# 20230325晚上跑的实验
#__________________________________________________20230325__________________________________________________________________
# python train.py --name c2d --data data/tea_single/c2d.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name depth --data data/tea_single/depth.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name ir --data data/tea_single/ir.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name rgbh --data data/tea_single/rgbh.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name rgbh_1280 --data data/tea_single/rgbh.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4 --img-size 1280 --device 0;

# python train.py --name c2d_ir_add --data data/tea_fusion/c2d_ir_add.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_ir_subtract --data data/tea_fusion/c2d_ir_subtract.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_ir_addWeighted --data data/tea_fusion/c2d_ir_addWeighted.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name ir_depth_addweighted --data data/tea_fusion/ir_depth_addweighted.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name c2d_ir_depth_aw --data data/tea_fusion/c2d_ir_depth_aw.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;

# python train.py --name buds_c2d_depth --data data/tea_copy_add/buds_c2d_depth.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name buds_c2d_ir --data data/tea_copy_add/buds_c2d_ir.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;

# python train.py --name rgba_c2d_depth --data data/tea_4h/rgba_c2d_depth.yaml  --cfg models/yolov5s_ch4.yaml --epochs 1500 --batch-size 4  --device 0;
# python train.py --name rgba_c2d_ir --data data/tea_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 1500 --batch-size 4  --device 0;


#运行一条_____________________________________________________________________
# python train.py --name c2d --data data/tea_single/c2d.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 0;
# python train.py --name depth --data data/tea_single/depth.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 0;
# python train.py --name ir --data data/tea_single/ir.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 0;
# python train.py --name rgbh --data data/tea_single/rgbh.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 0;
# python train.py --name rgbh_1280 --data data/tea_single/rgbh.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2 --img-size 1280 --device 0;
# python train.py --name buds_c2d_depth --data data/tea_copy_add/buds_c2d_depth.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 0;
# python train.py --name buds_c2d_ir --data data/tea_copy_add/buds_c2d_ir.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 0;

# python train.py --name c2d_ir_add --data data/tea_fusion/c2d_ir_add.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 1;
# python train.py --name c2d_ir_subtract --data data/tea_fusion/c2d_ir_subtract.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 1;
# python train.py --name c2d_ir_addWeighted --data data/tea_fusion/c2d_ir_addWeighted.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 1;
# python train.py --name ir_depth_addweighted --data data/tea_fusion/ir_depth_addweighted.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 1;
# python train.py --name c2d_ir_depth_aw --data data/tea_fusion/c2d_ir_depth_aw.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 2  --device 1;
# python train.py --name rgba_c2d_depth --data data/tea_4h/rgba_c2d_depth.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2500 --batch-size 4  --device 0;
# python test.py  --data data/tea_4h/rgba_c2d_depth.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\rgba_c2d_depth2\weights\best.pt --device 0
# python test.py  --data data/tea_4h/rgba_c2d_depth.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\rgba_c2d_depth\weights\best.pt --device 0

# python train.py --name rgba_c2d_ir --data data/tea_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2500 --batch-size 4  --device 0;
# python test.py  --data data/tea_4h/rgba_c2d_ir.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\rgba_c2d_ir\weights\best.pt --device 0
# python test.py  --data data/tea_4h/rgba_c2d_ir.yaml --weights D:\帅璐宇\RGBD_TEA\yolov5_4h\rgba_c2d_ir\weights\best.pt --device 0


# python train.py --name rgba_c2d_ir --data data/tea_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2500 --batch-size 4  --device 0;python train.py --name rgba_c2d_depth --data data/tea_4h/rgba_c2d_depth.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2500 --batch-size 4  --device 0;


#运行一条_____________________________________________________________________
# python train.py --name c2d --data data/tea_single/c2d.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;python train.py --name depth --data data/tea_single/depth.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0; python train.py --name ir --data data/tea_single/ir.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;python train.py --name rgbh --data data/tea_single/rgbh.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;python train.py --name rgbh_1280 --data data/tea_single/rgbh.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4 --img-size 1280 --device 0;python train.py --name buds_c2d_depth --data data/tea_copy_add/buds_c2d_depth.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;python train.py --name buds_c2d_ir --data data/tea_copy_add/buds_c2d_ir.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 0;

# python train.py --name c2d_ir_add --data data/tea_fusion/c2d_ir_add.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 1; python train.py --name c2d_ir_subtract --data data/tea_fusion/c2d_ir_subtract.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 1; python train.py --name c2d_ir_addWeighted --data data/tea_fusion/c2d_ir_addWeighted.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 1; python train.py --name ir_depth_addweighted --data data/tea_fusion/ir_depth_addweighted.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 1; python train.py --name c2d_ir_depth_aw --data data/tea_fusion/c2d_ir_depth_aw.yaml --cfg models/yolov5s_new.yaml --epochs 1500 --batch-size 4  --device 1; python train.py --name rgba_c2d_depth --data data/tea_4h/rgba_c2d_depth.yaml  --cfg models/yolov5s_ch4.yaml --epochs 1500 --batch-size 4  --device 1; python train.py --name rgba_c2d_ir --data data/tea_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 1500 --batch-size 4  --device 1;

# 20230406
# python train.py --name t1_rgba_c2d_depth --data data/tea_4h/rgba_c2d_depth.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 0;
# python train.py --name t1_rgba_c2d_ir --data data/tea_4h/rgba_c2d_ir.yaml  --cfg models/yolov5s_ch4.yaml --epochs 2000 --batch-size 4  --device 0;
