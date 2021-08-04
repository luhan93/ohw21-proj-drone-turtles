import numpy as np

from typing import Iterable


class BBox:
    def __init__(
        self, lower_x: float, lower_y: float, upper_x: float, upper_y: float
    ) -> None:
        self._lower_x = lower_x
        self._lower_y = lower_y
        self._upper_x = upper_x
        self._upper_y = upper_y

    @property
    def lower_x(self):
        return self._lower_x

    @property
    def lower_y(self):
        return self._lower_y

    @property
    def upper_x(self):
        return self._upper_x

    @property
    def upper_y(self):
        return self._upper_y


class ImageMetadata:
    def __init__(self, labels: Iterable[int], boxes: Iterable[BBox]):
        self._labels = labels
        self._boxes = boxes

    @property
    def labels(self) -> Iterable[int]:
        return self._labels

    @property
    def boxes(self) -> Iterable[BBox]:
        return self._boxes


class Batch:
    def __init__(
        self, raw: np.ndarray, metadata: Iterable[ImageMetadata]
    ) -> None:
        self._raw = raw
        self._metadata = metadata

    @property
    def raw(self) -> np.ndarray:
        return self._raw

    @property
    def metadata(self) -> Iterable[ImageMetadata]:
        return self._metadata
