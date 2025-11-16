# memory_bank.py
from typing import List, Dict
import hashlib
import json

class MemoryBank:
    def __init__(self):
        self.store = {}  # simple dict store; replace with persistence or vector DB

    def _make_key(self, user_id, key):
        return f"{user_id}:{key}"

    def get(self, user_id, key):
        return self.store.get(self._make_key(user_id, key))

    def set(self, user_id, key, value):
        self.store[self._make_key(user_id, key)] = value

    def append_mastery(self, user_id, topic, score):
        k = self._make_key(user_id, "mastery")
        self.store.setdefault(k, {})
        self.store[k][topic] = score

    def get_top_weak_topics(self, user_id, n=3):
        k = self._make_key(user_id, "mastery")
        mastery = self.store.get(k, {})
        sorted_items = sorted(mastery.items(), key=lambda x: x[1])
        return [t for t,_ in sorted_items[:n]]
