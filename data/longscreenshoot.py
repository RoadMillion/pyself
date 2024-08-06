import cv2
import numpy as np
from PIL import Image

def extract_frames(video_path, skip_frames=30):
    """
    从视频中提取帧。
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % skip_frames == 0:
            frames.append(frame)
        count += 1
    cap.release()
    return frames

def find_overlap_start_with_orb(img1, img2, max_features=500, good_match_percent=0.15):
    """
    使用ORB特征匹配来找到两个图像间重叠的起始点。
    """
    # 初始化ORB检测器
    orb = cv2.ORB_create(max_features)
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    # 匹配特征点
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # 按照匹配的距离排序
    matches = sorted(matches, key=lambda x: x.distance)

    # 移除不好的匹配结果
    numGoodMatches = int(len(matches) * good_match_percent)
    good_matches = matches[:numGoodMatches]

    # 提取匹配点的位置
    points1 = np.zeros((len(good_matches), 2), dtype=np.float32)
    points2 = np.zeros((len(good_matches), 2), dtype=np.float32)

    for i, match in enumerate(good_matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    if points2.any():
        overlap_start = np.min(points2[:, 1])  # 基于y坐标找到重叠的最小起始点
    else:
        overlap_start = 0

    return int(overlap_start)

def concatenate_images(images):
    """
    拼接图像列表，考虑去除重复的头部。
    """
    final_img = images[0]
    for i in range(1, len(images)):
        img1 = cv2.cvtColor(final_img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
        overlap_start = find_overlap_start_with_orb(img1, img2)
        if overlap_start > 0 and overlap_start < img2.shape[0]:
            non_overlap_part = images[i][overlap_start:, :]
            final_img = np.vstack((final_img, non_overlap_part))
        elif overlap_start >= img2.shape[0]:
            continue  # 如果重叠起始点在图像底部或之后，意味着没有新内容需要添加
        else:
            final_img = np.vstack((final_img, images[i]))
    return final_img

def generate_long_screenshot(video_path, skip_frames=30):
    """
    生成长截图。
    """
    frames = extract_frames(video_path, skip_frames)
    long_screenshot = concatenate_images(frames)
    cv2.imwrite('long_screenshot.png', long_screenshot)

# 使用示例
video_path = 'D:/download/screen.mp4'
generate_long_screenshot(video_path, skip_frames=50)

