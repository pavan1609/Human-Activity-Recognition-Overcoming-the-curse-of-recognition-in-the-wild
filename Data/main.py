import os
import time
import numpy as np
import pandas as pd
from data_loading import load_data, label_dict
from dtw_segmentations import dtw_distance, dtw_segmentation, segment_data
from verification import (
    plot_segments,
    check_segment_lengths,
    statistical_analysis,
    manual_inspection,
    check_outliers,
    check_transition_points
)

if __name__ == "__main__":
    data_folder = r'D:\PAVAN\WEAR\wearchallenge_hasca2024\wearchallenge_hasca2024'
    all_data = load_data(data_folder)

    # Adjusted parameters
    window_size = 10  # You can change this to test different window sizes
    threshold = 5.0  # You can change this to test different thresholds

    print(f"Running segmentation with window size: {window_size} and threshold: {threshold}")

    # Measure the time taken for segmentation
    start_time = time.time()
    subject_ids, segmented_data, segmented_labels = segment_data(all_data, window_size, threshold)
    end_time = time.time()

    print(f"Segmentation completed in {end_time - start_time:.2f} seconds")

    # Check shapes
    print(f"Shape of Subject IDs: {np.array(subject_ids).shape}")
    print(f"Number of Segmented Data: {len(segmented_data)} segments")
    print(f"Number of Segmented Labels: {len(segmented_labels)} labels")
    # Save segmented data
    save_folder = r'D:\PAVAN\WEAR\wearchallenge_hasca2024\output'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    np.save(os.path.join(save_folder, 'segmented_data.npy'), segmented_data)
    np.save(os.path.join(save_folder, 'subject_ids.npy'), subject_ids)
    np.save(os.path.join(save_folder, 'segmented_labels.npy'), segmented_labels)

    print(f"Segmented data saved to {save_folder}")

  
    # Verification
    plot_segments(segmented_data, segmented_labels, n=5)
    check_segment_lengths(segmented_data, window_size)
    statistical_analysis(segmented_data)
    manual_inspection(segmented_data, segmented_labels, start_idx=0, end_idx=10)
    check_outliers(segmented_data)
    check_transition_points(segmented_data, segmented_labels)
