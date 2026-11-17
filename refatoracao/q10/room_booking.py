from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class BookingRequest:
    building: str
    floor: int
    room: str
    start_hour: int
    end_hour: int
    projector: bool
    sound: bool
    attendees: int

    @property
    def duration_hours(self) -> int:
        return self.end_hour - self.start_hour


class RoomBooking:

    def quote(self, request: BookingRequest) -> float:
        base = request.duration_hours * 50.0

        if request.projector:
            base += 30.0
        if request.sound:
            base += 20.0
        if request.attendees > 40:
            base *= 1.15

        if request.building == "A" and request.floor >= 3:
            base += 10.0
        if request.room == "LAB":
            base += 40.0
            
        return round(base, 2)
