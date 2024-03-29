from typing import Sequence

import numpy as np
from numpy._typing import NDArray
from scipy.signal import resample


def calculate_frequency(key: int, reference_key=49, reference_freq=440.0) -> float:
    """
    Calculate the frequency of a musical note given its key number on the piano.

    Args:
    key (int): The key number (e.g., A4 is 49, C4 is 40).
    reference_key (int): The reference key number (A4 is 49).
    reference_freq (float): The frequency of the reference key (A4 is 440 Hz).

    Returns:
    float: The frequency of the note.
    """
    return reference_freq * 2 ** ((key - reference_key) / 12)


def snap_nearest_index(value: float, options: Sequence[float]) -> int:
    nearest_index = 0
    smallest_diff = abs(value - options[0])

    for i, option in enumerate(options[1:], start=1):
        current_diff = abs(value - option)

        if current_diff < smallest_diff:
            nearest_index = i
            smallest_diff = current_diff

    return nearest_index


def resample_to_size(audio_data: NDArray, factor: float) -> np.ndarray:
    if len(audio_data.shape) == 1:
        return resample(audio_data, num=int(len(audio_data) * factor))

    channels = audio_data.shape[0]
    resampled_data = [resample(audio_data[c], num=int(len(audio_data[c]) * factor)) for c in range(channels)]
    return np.array(resampled_data, dtype=np.float32)


NOTE_FREQUENCIES = tuple(calculate_frequency(key) for key in range(16, 89))
