from typing import List


class Video:
    def __init__(self):
        self.name = None

    def create(self, name: str) -> None:
        self.name = name

    def play(self) -> None:
        print(f'воспроизведение видео {self.name}')
        

class YouTube:
    videos: List[Video] = []

    @classmethod
    def add_video(cls, video: Video) -> None:
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx: int) -> None:
        cls.videos[video_indx].play()


v1 = Video()
v1.create("Python")
v2 = Video()
v2.create("Python ООП")

YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play(0)
YouTube.play(1)