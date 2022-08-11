from typing import Union, List, Tuple


class TrackLine:
    def __init__(self, to_x: Union[int, float], to_y: Union[int, float], max_speed: int):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x: Union[int, float], start_y: Union[int, float]):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks: List[TrackLine] = []
        self._len: float = 0

    @staticmethod
    def dist(x1, y1, x2, y2) -> float:
        return ((x2 - x1)**2 + (y2 - y1)**2)**.5

    def add_track(self, tr: TrackLine) -> None:
        if not self.tracks:
            self._len += self.dist(self.start_x, self.start_y, tr.to_x, tr.to_y)
        else:
            self._len += self.dist(self.tracks[-1].to_x, self.tracks[-1].to_y, tr.to_x, tr.to_y)
        self.tracks.append(tr)

    def get_tracks(self) -> Tuple[TrackLine, ...]:
        return tuple(self.tracks)

    def __len__(self):
        return int(self._len)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2 = Track(0, 1)
track1.add_track(TrackLine(3, 2, 90))
track1.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
