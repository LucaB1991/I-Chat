from typing import Any, Dict, Optional, Text
import time


class Event:
    """base class for event implementation"""
    category = 'root'

    @staticmethod
    def search_by_category():
        pass

    def __init__(self,
                 timestamp: Optional[float] = None,
                 data: Optional[Dict[Text, Any]] = None) -> None:
        self._timestamp = timestamp or time.time()
        self._data = data or {}

    @property
    def data(self) -> Dict[Text, Any]:
        return getattr(self, '_data', {})

    def as_dict(self) -> Dict[Text, Any]:
        output_dict = {
            'category': self.category,
            'timestamp': self._timestamp
        }
        if self._data:
            output_dict['data'] = self._data
        return output_dict

    def apply_to_tracker(self, tracker: "DialogStateTracker") -> None:
        """This method must be overwritten to log the event to the the tracker."""
        pass
