#helper logic for detection pipeline filtring & formatting

#check if detected class is alloweed
def is_vehicle(clss_id,allowed_class_ids):
    return clss_id in allowed_class_ids

def format_detections(x1,y1,x2,y2,conf,clss_id):
    return {
        "bbox":[x1,y1,x2,y2],
        "confidence":conf,
        "class_id":clss_id
    }
    