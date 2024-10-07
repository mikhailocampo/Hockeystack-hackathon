from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing import List


class Views(str, Enum):
    OVERVIEW = "overview"
    INGRESS = "ingress"
    DETAILED = "detailed_view"


class Clip(BaseModel):
    clip_transcription: str = Field(..., description="Full transcript of the clip")
    start_time: str = Field(..., description="Start time of the clip")
    end_time: str = Field(..., description="End time of the clip")
    delta: float = Field(..., description="Delta between -1 and 1 representing the sentiment of the clip")


class Analysis(BaseModel):
    clips: List[Clip] = Field(..., description="List of clips extracted from the video")
    key_summary: List[str] = Field(..., description="List of key summary points extracted from the video and clips")
    
    def calculate_sum(self):
        if not self.clips:
            self.sum = 0.0
        else:
            self.sum = sum(clip.delta for clip in self.clips)

