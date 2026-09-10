import cv2

def enhance_tactical_frame(frame):
    """Applies adaptive contrast to help the AI see through dark/foggy frames."""
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l_channel, a, b = cv2.split(lab)
    
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l_channel)
    
    lmerge = cv2.merge((cl, a, b))
    enhanced_frame = cv2.cvtColor(lmerge, cv2.COLOR_LAB2BGR)
    return enhanced_frame
