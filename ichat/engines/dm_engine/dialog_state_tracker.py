from typing import Any, Dict, Iterable, Text, List, Optional
from .slots import Slot
from .events import Event
from ichat.utils.constants import ACTION_LISTEN


class DialogStateTracker:
    """It keeps track of the conversation"""

    def __init__(self,
                 message_sender_id: Text,
                 events: List[Event],
                 slots: Optional[Iterable[Slot]],
                 maximum_events_history: Optional[int] = None
                 ) -> None:
        self._paused = False
        self.latest_user_message = None
        self.latest_system_message = None
        self.latest_action = None
        self.next_action = ACTION_LISTEN
