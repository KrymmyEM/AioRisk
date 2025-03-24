from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List

from ..enums import ChannelState

class BasicModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class AsteriskPing(BasicModel):
    asterisk_id: str = Field(..., description="Asterisk id info")
    ping: str = Field(..., description="Always string value is pong")
    timestamp: str = Field(..., description="The timestamp string of request received time")

class BuildInfo(BasicModel):
    date: str = Field(..., description="Date and time when Asterisk was built.")
    kernel: str = Field(..., description="Kernel version Asterisk was built on.")
    machine: str = Field(..., description="Machine architecture (x86_64, i686, ppc, etc.)")
    options: str = Field(..., description="Compile time options, or empty string if default.")
    os: str = Field(..., description="OS Asterisk was built on.")
    user: str = Field(..., description="Username that build Asterisk")


class ConfigTuple(BasicModel):
    attribute: str = Field(..., description="A configuration object attribute.")
    value: str = Field(..., description="The value for the attribute.")

class LogChannel(BasicModel):
    channel: str = Field(..., description="The log channel path")
    configuration: str = Field(..., description="The various log levels")
    status: str = Field(..., description="Whether or not a log type is enabled")
    type_: str = Field(..., description="Types of logs for the log channel", alias="type")

class Module(BasicModel):
    description: str = Field(..., description="The description of this module")
    name: str = Field(..., description="The name of this module")
    status: str = Field(..., description="The running status of this module")
    support_level: str = Field(..., description="The support state of this module")
    use_count: int = Field(..., description="The number of times this module is being used")

class SetId(BasicModel):
    group: str = Field(..., description="Effective group id.")
    user: str = Field(..., description="Effective user id.")


class ConfigInfo(BasicModel):
    default_language: str = Field(..., description="Default language for media playback.")
    max_channels: Optional[int] = Field(None, description="Maximum number of simultaneous channels.")
    max_load: Optional[float] = Field(None, description="Maximum load avg on system.")
    max_open_files: Optional[int] = Field(None, description="Maximum number of open file handles (files, sockets).")
    name: str = Field(..., description="Asterisk system name.")
    setid: SetId = Field(..., description="Effective user/group id for running Asterisk.")


class StatusInfo(BasicModel):
    last_reload_time: str = Field(..., description="Time when Asterisk was last reloaded.")
    startup_time: str = Field(..., description="Time when Asterisk was started.")

class SystemInfo(BasicModel):
    entity_id: str = Field(..., description="")
    version: str = Field(..., description="Asterisk version.")

class AsteriskInfo(BasicModel):
    build: Optional[BuildInfo] = Field(None, description="Info about how Asterisk was built")
    config: Optional[ConfigInfo] = Field(None, description="Info about Asterisk configuration")
    status: Optional[StatusInfo] = Field(None, description="Info about Asterisk status")
    system: Optional[SystemInfo] = Field(None, description="Info about the system running Asterisk")

class Variable(BasicModel):
    value: str = Field(..., description="The value of the variable requested")

class Endpoint(BasicModel):
    channel_ids: List[str] = Field(..., description="Id's of channels associated with this endpoint")
    resource: str = Field(..., description="Identifier of the endpoint, specific to the given technology.")
    state: Optional[str] = Field(None, description="Endpoint's state")
    technology: str = Field(..., description="Technology of the endpoint")

class TextMessage(BasicModel):
    body: str = Field(..., description="The text of the message.")
    from_: str = Field(..., description="A technology specific URI specifying the source of the message. For pjsip technology, any SIP URI can be specified. For xmpp, the URI must correspond to the client connection being used to send the message.", alias="from")
    to_: str = Field(..., description="A technology specific URI specifying the destination of the message. Valid technologies include pjsip, and xmp. The destination of a message should be an endpoint.", alias="to")
    variables: Optional[dict] = Field(None, description="Technology specific key/value pairs (JSON object) associated with the message.")

class CallerID(BasicModel):
    name: str = Field(..., description="")
    number: str = Field(..., description="")

class Dialed(BasicModel):
    app_data: str = Field(..., description="Parameter of current dialplan application")
    app_name: str = Field(..., description="Name of current dialplan application")
    context: str = Field(..., description="Context in the dialplan")
    exten: str = Field(..., description="Extension in the dialplan")
    priority: int = Field(..., description="Priority in the dialplan")

class DialplanCEP(BasicModel):
    app_data: str = Field(..., description="Parameter of current dialplan application")
    app_name: str = Field(..., description="Name of current dialplan application")
    context: str = Field(..., description="Context in the dialplan")
    exten: str = Field(..., description="Extension in the dialplan")
    priority: int = Field(..., description="Priority in the dialplan")


class Channel(BasicModel):
    id_: str = Field(..., description="Unique identifier of the channel.", alias="id")
    protocol_id: str = Field(..., description="(string): Protocol id from underlying channel driver (i.e. Call-ID for chan_pjsip; will be empty if not applicable or not implemented by driver).")
    accountcode: str = Field(..., description="")
    caller: CallerID = Field(..., description="")
    caller_rdnis: Optional[str] = Field(None, description="The Caller ID RDNIS")
    channelvars: Optional[dict] = Field(None, description="Channel variables")
    connected: CallerID = Field(..., description="")
    creationtime: str = Field(..., description="Timestamp when channel was created")
    dialplan: DialplanCEP = Field(..., description="Current location in the dialplan")
    name: str = Field(..., description="(string): Name of the channel (i.e. SIP/foo-0000a7e3)")
    state: ChannelState = Field(..., description="(string) = ['Down' or 'Rsrved' or 'OffHook' or 'Dialing' or 'Ring' or 'Ringing' or 'Up' or 'Busy' or 'Dialing Offhook' or 'Pre-ring' or 'Unknown'],")
    language: str = Field(..., description="#(string): The default spoken language,")
    tenantid: Optional[str] = Field(None, description="#(string, optional): The Tenant ID for the channel")

    class Config:
        use_enum_values = True

class RTPstat(BasicModel):
    channel_uniqueid: str = Field(..., description="The Asterisk channel's unique ID that owns this instance.")
    local_maxjitter: Optional[float] = Field(None, description="Maximum jitter on local side.")
    local_maxrxploss: Optional[float] = Field(None, description="Maximum number of packets lost on local side.")
    local_minjitter: Optional[float] = Field(None, description="Minimum jitter on local side.")
    local_minrxploss: Optional[float] = Field(None, description="Minimum number of packets lost on local side.")
    local_normdevjitter: Optional[float] = Field(None, description="Average jitter on local side.")
    local_normdevrxploss: Optional[float] = Field(None, description="Average number of packets lost on local side.")
    local_ssrc: int = Field(..., description="Our SSRC.")
    local_stdevjitter: Optional[float] = Field(None, description="Standard deviation jitter on local side.")
    local_stdevrxploss: Optional[float] = Field(None, description="Standard deviation packets lost on local side.")
    maxrtt: Optional[float] = Field(None, description="Maximum round trip time.")
    minrtt: Optional[float] = Field(None, description="Minimum round trip time.")
    normdevrtt: Optional[float] = Field(None, description="Average round trip time.")
    remote_maxjitter: Optional[float] = Field(None, description="Maximum jitter on remote side.")
    remote_maxrxploss: Optional[float] = Field(None, description="Maximum number of packets lost on remote side.")
    remote_minjitter: Optional[float] = Field(None, description="Minimum jitter on remote side.")
    remote_minrxploss: Optional[float] = Field(None, description="Minimum number of packets lost on remote side.")
    remote_normdevjitter: Optional[float] = Field(None, description="Average jitter on remote side.")
    remote_normdevrxploss: Optional[float] = Field(None, description="Average number of packets lost on remote side.")
    remote_ssrc: int = Field(..., description="Their SSRC.")
    remote_stdevjitter: Optional[float] = Field(None, description="Standard deviation jitter on remote side.")
    remote_stdevrxploss: Optional[float] = Field(None, description="Standard deviation packets lost on remote side.")
    rtt: Optional[float] = Field(None, description="Total round trip time.")
    rxcount: int = Field(..., description="Number of packets received.")
    rxjitter: Optional[float] = Field(None, description="Jitter on received packets.")
    rxoctetcount: int = Field(..., description="Number of octets received.")
    rxploss: int = Field(..., description="Number of received packets lost.")
    stdevrtt: Optional[float] = Field(None, description="Standard deviation round trip time.")
    txcount: int = Field(..., description="Number of packets transmitted.")
    txjitter: Optional[float] = Field(None, description="Jitter on transmitted packets.")
    txoctetcount: int = Field(..., description="Number of octets transmitted.")
    txploss: int = Field(..., description="Number of transmitted packets lost.")

class Bridge(BasicModel):
    bridge_class: str = Field(..., description="Bridging class")
    bridge_type: str = Field(..., description="Type of bridge technology")
    channels: List[str] = Field(..., description="Ids of channels participating in this bridge")
    creationtime: str = Field(..., description="Timestamp when bridge was created")
    creator: str = Field(..., description="Entity that created the bridge")
    id_: str = Field(..., description="Unique identifier for this bridge", alias="id")
    name: str = Field(..., description="Name the creator gave the bridge")
    technology: str = Field(..., description="Name of the current bridging technology")
    video_mode: Optional[str] = Field(None, description="The video mode the bridge is using. One of 'none', 'talker', 'sfu', or 'single'.")
    video_source_id: Optional[str] = Field(None, description="The ID of the channel that is the source of video in this bridge, if one exists.")

class LiveRecording(BasicModel):
    cause: Optional[str] = Field(None, description="Cause for recording failure if failed")
    duration: Optional[int] = Field(None, description="Duration in seconds of the recording")
    format: str = Field(..., description="Recording format (wav, gsm, etc.)")
    name: str = Field(..., description="Base name for the recording")
    silence_duration: Optional[int] = Field(None, description="Duration of silence, in seconds, detected in the recording. This is only available if the recording was initiated with a non-zero maxSilenceSeconds.")
    state: str = Field(..., description="")
    talking_duration: Optional[int] = Field(None, description="Duration of talking, in seconds, detected in the recording. This is only available if the recording was initiated with a non-zero maxSilenceSeconds.")
    target_uri: str = Field(..., description="URI for the channel or bridge being recorded")

class StoredRecording(BasicModel):
    format: str = Field(..., description="")
    name: str = Field(..., description="")

class FormatLangPair(BasicModel):
    format: str = Field(..., description="")
    language: str = Field(..., description="")

class Sound(BasicModel):
    formats: List[FormatLangPair] = Field(..., description="The formats and languages in which this sound is available.")
    id_: str = Field(..., description="Sound's identifier.", alias="id")
    text: Optional[str] = Field(None, description="Text description of the sound, usually the words spoken.")

class Playback(BasicModel):
    id_: str = Field(..., description="ID for this playback operation", alias="id")
    language: Optional[str] = Field(None, description="For media types that support multiple languages, the language requested for playback.")
    media_uri: str = Field(..., description="The URI for the media currently being played back.")
    next_media_uri: Optional[str] = Field(None, description="If a list of URIs is being played, the next media URI to be played back.")
    state: str = Field(..., description="Current state of the playback operation.")
    target_uri: str = Field(..., description="URI for the channel or bridge to play the media on")

class DeviceState(BasicModel):
    name: str = Field(..., description="Name of the device.")
    state: str = Field(..., description="Device's state")

class Mailbox(BasicModel):
    name: str = Field(..., description="Name of the mailbox.")
    new_messages: int = Field(..., description="Count of new messages in the mailbox.")
    old_messages: int = Field(..., description="Count of old messages in the mailbox.")

class AdditionalParam(BasicModel):
    parameter_name: str = Field(..., description="Name of the parameter")
    parameter_value: str = Field(..., description="Value of the parameter")

class ContactInfo(BasicModel):
    aor: str = Field(..., description="The Address of Record this contact belongs to.")
    contact_status: str = Field(..., description="The current status of the contact.")
    roundtrip_usec: Optional[str] = Field(None, description="Current round trip time, in microseconds, for the contact.")
    uri: str = Field(..., description="The location of the contact.")

class Peer(BasicModel):
    address: Optional[str] = Field(None, description="The IP address of the peer.")
    cause: Optional[str] = Field(None, description="An optional reason associated with the change in peer_status.")
    peer_status: str = Field(..., description="The current state of the peer. Note that the values of the status are dependent on the underlying peer technology.")
    port: Optional[str] = Field(None, description="The port of the peer.")
    time: Optional[str] = Field(None, description="The last known time the peer was contacted.")

class ReferredBy(BasicModel):
    bridge: Optional[Bridge] = Field(None, description="Bridge connecting both Channels")
    connected_channel: Optional[Channel] = Field(None, description="Channel, Connected to the channel, receiving the transfer request on.")
    source_channel: Channel = Field(..., description="The channel on which the refer was received")

class RequiredDestination(BasicModel):
    additional_protocol_params: Optional[List[AdditionalParam]] = Field(None, description="List of additional protocol specific information")
    destination: Optional[str] = Field(None, description="Destination User Part. Only for Blind transfer. Mutually exclusive to protocol_id")
    protocol_id: Optional[str] = Field(None, description="the requested protocol-id by the referee in case of SIP channel, this is a SIP Call ID, Mutually exclusive to destination")

class ReferTo(BasicModel):
    bridge: Optional[Bridge] = Field(None, description="Bridge connecting both destination channels")
    connected_channel: Optional[Channel] = Field(None, description="Channel, connected to the to be replaced channel")
    destination_channel: Optional[Channel] = Field(None, description="The Channel Object, that is to be replaced")
    requested_destination: RequiredDestination = Field(..., description="")

class Application(BasicModel):
    bridge_ids: List[str] = Field(..., description="Id's for bridges subscribed to.")
    channel_ids: List[str] = Field(..., description="Id's for channels subscribed to.")
    device_names: List[str] = Field(..., description="Names of the devices subscribed to.")
    endpoint_ids: List[str] = Field(..., description="{tech}/{resource} for endpoints subscribed to.")
    events_allowed: List[dict] = Field(..., description="Event types sent to the application.")
    events_disallowed: List[dict] = Field(..., description="Event types not sent to the application.")
    name: str = Field(..., description="Name of this application")


class Message(BasicModel):
    asterisk_id: Optional[str] = Field(None, description="The unique ID for the Asterisk instance that raised this event.")
    type_: str = Field(..., description="Indicates the type of this message.", alias="type")

class MissingParams(Message):
    params: List[str] = Field(..., description="A list of the missing parameters")

class Event(Message):
    application: str = Field(..., description="Name of the application receiving the event.")
    timestamp: str = Field(..., description="Time at which this event was created.")

