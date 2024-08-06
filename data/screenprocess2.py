import os
import sys

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def extract_frames(video_path, scale_factor=1.0):
    frames = []
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if scale_factor != 1.0:
            frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
        frames.append(frame)
    cap.release()
    return frames


def is_duplicate_frame(frame1, frame2, threshold=0.95):
    if frame1 is None or frame2 is None:
        return False
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    sim = ssim(gray1, gray2)
    return sim > threshold


def find_overlap(frame1, frame2, status_bar_height=50):
    if frame1 is None or frame2 is None:
        return 0, 0
    gray1 = cv2.cvtColor(frame1[status_bar_height:, :], cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2[status_bar_height:, :], cv2.COLOR_BGR2GRAY)
    height = gray1.shape[0]
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    if len(matches) > 0:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        h, w = gray1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)
        overlap_top = max(0, int(dst[0][0][1]))
        overlap_bottom = min(height, int(dst[2][0][1]))
        return status_bar_height + overlap_top, status_bar_height + overlap_bottom
    else:
        return 0, 0


def blend_overlap_region(img1, img2, overlap_top, overlap_bottom):
    overlap_height = overlap_bottom - overlap_top
    alpha = np.linspace(0, 1, overlap_height, dtype=np.float64)
    blended_overlap = np.zeros_like(img1[overlap_top:overlap_bottom, :], dtype=np.uint8)
    for i in range(overlap_height):
        blended_overlap[i, :] = (
                img1[overlap_top + i, :] * (1 - alpha[i]) + img2[overlap_top + i, :] * alpha[i]).astype(np.uint8)
    return blended_overlap


def stitch_frames(frames, status_bar_height=50, block_size=10):
    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)
    stitched_blocks = []
    for i in range(0, len(frames), block_size):
        block_frames = frames[i:i + block_size]
        stitched_block = None
        for frame in block_frames:
            if stitched_block is None:
                stitched_block = frame
            else:
                if not is_duplicate_frame(stitched_block[-status_bar_height:, :], frame[:status_bar_height, :]):
                    result, pano = stitcher.stitch([stitched_block, frame])
                    if result == cv2.STITCHER_OK:
                        stitched_block = pano
                    else:
                        stitched_block = cv2.vconcat([stitched_block, frame[status_bar_height:, :]])
        stitched_blocks.append(stitched_block)

    stitched_image = stitched_blocks[0]
    for block in stitched_blocks[1:]:
        stitched_image = cv2.vconcat([stitched_image, block[status_bar_height:, :]])

    return stitched_image


def generate_long_screenshot(video_path, output_path, scale_factor=1.0, max_frames_per_stitch=100):
    try:
        frames = extract_frames(video_path, scale_factor)
        long_screenshot = stitch_frames(frames, max_frames_per_stitch)
        cv2.imwrite(output_path, long_screenshot)
        print(f"Long screenshot generated successfully: {output_path}")
    except Exception as e:
        print(f"Error generating long screenshot: {str(e)}")


def validate_input(video_path, output_path):
    if not os.path.isfile(video_path):
        print(f"Video file does not exist: {video_path}")
        return False
    if not output_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        print("Output file must have a valid image extension (jpg, jpeg, png)")
        return False
    return True


if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print("Usage: python script.py <video_path> <output_path>")
    #     sys.exit(1)
    video_path = 'D:/download/screen.mp4'
    output_path = 'a3312.png'
    if not validate_input(video_path, output_path):
        sys.exit(1)
    generate_long_screenshot(video_path, output_path, scale_factor=0.3, max_frames_per_stitch=50)
