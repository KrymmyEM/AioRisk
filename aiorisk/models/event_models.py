from pydantic import Field
from typing import Optional, List

from ..models.base_models import *


class PeerStatusChange(Event):
    endpoint: Endpoint = Field(..., description="")
    peer: Peer = Field(..., description="")

class PlaybackContinuing(Event):
    playback: Playback = Field(..., description="Playback control object")

class PlaybackFinished(Event):
    playback: Playback = Field(..., description="Playback control object")

class PlaybackStarted(Event):
    playback: Playback = Field(..., description="Playback control object")

class RecordingFailed(Event):
    recording: LiveRecording = Field(..., description="Recording control object")

class RecordingFinished(Event):
    recording: LiveRecording = Field(..., description="Recording control object")

class RecordingStarted(Event):
    recording: LiveRecording = Field(..., description="Recording control object")

class StasisEnd(Event):
    channel: Channel = Field(..., description="")

class StasisStart(Event):
    args: List[str] = Field(..., description="Arguments to the application")
    channel: Channel = Field(..., description="")
    replace_channel: Optional[Channel] = Field(None, description="")

class TextMessageReceived(Event):
    endpoint: Optional[Endpoint] = Field(None, description="")
    message: TextMessage = Field(..., description="")

class ApplicationMoveFailed(Event):
    args: List[str] = Field(..., description="Arguments to the application")
    channel: Channel = Field(..., description="")
    destination: str = Field(..., description="")

class ApplicationReplaced(Event):
    pass

class BridgeAttendedTransfer(Event):
    destination_application: Optional[str] = Field(None, description="Application that has been transferred into")
    destination_bridge: Optional[str] = Field(None, description="Bridge that survived the merge result")
    destination_link_first_leg: Optional[Channel] = Field(None, description="First leg of a link transfer result")
    destination_link_second_leg: Optional[Channel] = Field(None, description="Second leg of a link transfer result")
    destination_threeway_bridge: Optional[Bridge] = Field(None, description="Bridge that survived the threeway result")
    destination_threeway_channel: Optional[Channel] = Field(None, description="Transferer channel that survived the threeway result")
    destination_type: str = Field(..., description="How the transfer was accomplished")
    is_external: bool = Field(..., description="Whether the transfer was externally initiated or not")
    replace_channel: Optional[Channel] = Field(None, description="The channel that is replacing transferer_first_leg in the swap")
    result: str = Field(..., description="The result of the transfer attempt")
    transfer_target: Optional[Channel] = Field(None, description="The channel that is being transferred to")
    transferee: Optional[Channel] = Field(None, description="The channel that is being transferred")
    transferer_first_leg: Channel = Field(..., description="First leg of the transferer")
    transferer_first_leg_bridge: Optional[Bridge] = Field(None, description="Bridge the transferer first leg is in")
    transferer_second_leg: Channel = Field(..., description="Second leg of the transferer")
    transferer_second_leg_bridge: Optional[Bridge] = Field(None, description="Bridge the transferer second leg is in")

class BridgeBlindTransfer(Event):
    bridge: Optional[Bridge] = Field(None, description="The bridge being transferred")
    channel: Channel = Field(..., description="The channel performing the blind transfer")
    context: str = Field(..., description="The context transferred to")
    exten: str = Field(..., description="The extension transferred to")
    is_external: bool = Field(..., description="Whether the transfer was externally initiated or not")
    replace_channel: Optional[Channel] = Field(None, description="The channel that is replacing transferer when the transferee(s) can not be transferred directly")
    result: str = Field(..., description="The result of the transfer attempt")
    transferee: Optional[Channel] = Field(None, description="The channel that is being transferred")

class BridgeCreated(Event):
    bridge: Bridge = Field(..., description="")

class BridgeDestroyed(Event):
    bridge: Bridge = Field(..., description="")

class BridgeMerged(Event):
    bridge: Bridge = Field(..., description="")
    bridge_from: Bridge = Field(..., description="")

class BridgeVideoSourceChanged(Event):
    bridge: Bridge = Field(..., description="")
    old_video_source_id: Optional[str] = Field(None, description="")

class ChannelCallerId(Event):
    caller_presentation: int = Field(..., description="The integer representation of the Caller Presentation value.")
    caller_presentation_txt: str = Field(..., description="The text representation of the Caller Presentation value.")
    channel: Channel = Field(..., description="The channel that changed Caller ID.")

class ChannelConnectedLine(Event):
    channel: Channel = Field(..., description="The channel whose connected line has changed.")

class ChannelCreated(Event):
    channel: Channel = Field(..., description="")

class ChannelDestroyed(Event):
    cause: int = Field(..., description="Integer representation of the cause of the hangup")
    cause_txt: str = Field(..., description="Text representation of the cause of the hangup")
    channel: Channel = Field(..., description="")

class ChannelDialplan(Event):
    channel: Channel = Field(..., description="The channel that changed dialplan location.")
    dialplan_app: str = Field(..., description="The application about to be executed.")
    dialplan_app_data: str = Field(..., description="The data to be passed to the application.")

class ChannelDtmfReceived(Event):
    channel: Channel = Field(..., description="The channel on which DTMF was received")
    digit: str = Field(..., description="DTMF digit received (0-9, A-E, # or *)")
    duration_ms: int = Field(..., description="Number of milliseconds DTMF was received")

class ChannelEnteredBridge(Event):
    bridge: Bridge = Field(..., description="")
    channel: Optional[Channel] = Field(None, description="")

class ChannelHangupRequest(Event):
    cause: Optional[int] = Field(None, description="Integer representation of the cause of the hangup.")
    channel: Channel = Field(..., description="The channel on which the hangup was requested.")
    soft: Optional[bool] = Field(None, description="Whether the hangup request was a soft hangup request.")

class ChannelHold(Event):
    channel: Channel = Field(..., description="The channel that initiated the hold event.")
    musicclass: Optional[str] = Field(None, description="The music on hold class that the initiator requested.")

class ChannelLeftBridge(Event):
    bridge: Bridge = Field(..., description="")
    channel: Channel = Field(..., description="")

class ChannelStateChange(Event):
    channel: Channel = Field(..., description="")

class ChannelTalkingFinished(Event):
    channel: Channel = Field(..., description="The channel on which talking completed.")
    duration: int = Field(..., description="The length of time, in milliseconds, that talking was detected on the channel")

class ChannelTalkingStarted(Event):
    channel: Channel = Field(..., description="The channel on which talking started.")

class ChannelToneDetected(Event):
    channel: Channel = Field(..., description="The channel the tone was detected on.")

class ChannelTransfer(Event):
    refer_to: ReferTo = Field(..., description="Refer-To information with optionally both affected channels")
    referred_by: ReferredBy = Field(..., description="Referred-By SIP Header according rfc3892")
    state: Optional[str] = Field(None, description="Transfer State")

class ChannelUnhold(Event):
    channel: Channel = Field(..., description="The channel that initiated the unhold event.")

class ChannelUserevent(Event):
    bridge: Optional[Bridge] = Field(None, description="A bridge that is signaled with the user event.")
    channel: Optional[Channel] = Field(None, description="A channel that is signaled with the user event.")
    endpoint: Optional[Endpoint] = Field(None, description="A endpoint that is signaled with the user event.")
    eventname: str = Field(..., description="The name of the user event.")
    userevent: dict = Field(..., description="Custom Userevent data")

class ChannelVarset(Event):
    channel: Optional[Channel] = Field(None, description="The channel on which the variable was set.")

class ContactStatusChange(Event):
    contact_info: ContactInfo = Field(..., description="")
    endpoint: Endpoint = Field(..., description="")

class DeviceStateChanged(Event):
    device_state: DeviceState = Field(..., description="Device state object")

class Dial(Event):
    caller: Optional[Channel] = Field(None, description="The calling channel.")
    dialstatus: str = Field(..., description="Current status of the dialing attempt to the peer.")
    dialstring: Optional[str] = Field(None, description="The dial string for calling the peer channel.")
    forward: Optional[str] = Field(None, description="Forwarding target requested by the original dialed channel.")
    forwarded: Optional[Channel] = Field(None, description="Channel that the caller has been forwarded to.")
    peer: Channel = Field(..., description="The dialed channel.")

class EndpointStateChange(Event):
    endpoint: Endpoint = Field(..., description="")
