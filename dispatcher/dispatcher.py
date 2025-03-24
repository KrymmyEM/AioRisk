import importlib
import asyncio
import json
from enum import Enum
from typing import Callable, Any, Union, List

import websockets

from ..enums import AsteriskEvent
from ..base.app import App


event_module = "..models.event_models"

event_models = importlib.import_module(event_module, package=__package__) 


class EventDispatcher:
    def __init__(self):
        self.event_handlers = {}

    def register(self, event_name: Union[str, AsteriskEvent], callback: Callable[..., Any]):
        """Register an event handler."""
        if not asyncio.iscoroutinefunction(callback):
            raise TypeError(f"Event handler for {event_name} must be an async function")
        if event_name not in AsteriskEvent:
            raise ValueError(f"Invalid event name: {event_name}")
        
        if isinstance(event_name, AsteriskEvent):
            event_name = event_name.value

        self.event_handlers[event_name] = callback

    async def dispatch_event(self, event: dict):
        event_name = event.get("type")
        if not event_name:
            return

        model_cls = getattr(event_models, event_name, None)
        if not model_cls:
            raise ValueError(f"Unknown event type: {event_name}")
        event_data = model_cls(**event)
        call = self.event_handlers.get(event_name, None)
        if call:
            await call(event_data)

    async def run(self, app: App):
        uri = app.events_uri
        async with websockets.connect(uri) as ws:
            try:
                async for message in ws:
                    event = json.loads(message)
                    try:
                        await self.dispatch_event(event)
                    except Exception as e:
                        pass
            except websockets.exceptions.ConnectionClosed as e:
                raise e
