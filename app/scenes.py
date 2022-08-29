from abc import ABC, abstractmethod
from enum import Enum
from typing import Any
from uuid import uuid4
from pydantic import BaseModel

class SceneType(Enum):
    none = None
    image = "Image"
    slideshow = "Slideshow"


class Scene(ABC):
    type = SceneType.none
    looping = True
    
    def __init__(self, name : str):
        self._name = name
        self.tag = uuid4()

    @property
    def name(self):
        return self._name

    @property
    def details(self):
        return

class ImageScene(Scene):
    type = SceneType.image

class SlideshowScene(Scene):
    type = SceneType.slideshow

    def __init__(self, *args, **kwargs):
        self.slides : list[dict[str, Any]] = []
        super().__init__(*args, **kwargs)
        
    def add_slide(self, slide : ImageScene, duration : float):
        self.slides.append({
            "slide": slide,
            "duration": duration
        })

    @property
    def total_duration(self):
        duration = 0
        for slide in self.slides:
            duration += slide.get("duration", 0)

        return duration

    @property
    def details(self):
        yield f"{len(self.slides)} Slides"
        yield f"{self.total_duration} sec. total duration"