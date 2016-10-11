#
# This file generated automatically from randr.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto
import render

MAJOR_VERSION = 1
MINOR_VERSION = 4

key = xcb.ExtensionKey('RANDR')

class OutputError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadOutput(xcb.ProtocolException):
    pass

class CrtcError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadCrtc(xcb.ProtocolException):
    pass

class ModeError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadMode(xcb.ProtocolException):
    pass

class ProviderError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)

class BadProvider(xcb.ProtocolException):
    pass

class Rotation:
    Rotate_0 = 1
    Rotate_90 = 2
    Rotate_180 = 4
    Rotate_270 = 8
    Reflect_X = 16
    Reflect_Y = 32

class ScreenSize(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.width, self.height, self.mwidth, self.mheight,) = unpack_from('HHHH', parent, offset)

class RefreshRates(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.nRates,) = unpack_from('H', parent, offset)
        offset += 2
        self.rates = xcb.List(parent, offset, self.nRates, 'H', 2)
        offset += len(self.rates.buf())
        xcb._resize_obj(self, offset - base)

class QueryVersionCookie(xcb.Cookie):
    pass

class QueryVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.major_version, self.minor_version,) = unpack_from('xx2x4xII16x', parent, offset)

class SetConfig:
    Success = 0
    InvalidConfigTime = 1
    InvalidTime = 2
    Failed = 3

class SetScreenConfigCookie(xcb.Cookie):
    pass

class SetScreenConfigReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.new_timestamp, self.config_timestamp, self.root, self.subpixel_order,) = unpack_from('xB2x4xIIIH10x', parent, offset)

class NotifyMask:
    ScreenChange = 1
    CrtcChange = 2
    OutputChange = 4
    OutputProperty = 8
    ProviderChange = 16
    ProviderProperty = 32
    ResourceChange = 64

class GetScreenInfoCookie(xcb.Cookie):
    pass

class GetScreenInfoReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.rotations, self.root, self.timestamp, self.config_timestamp, self.nSizes, self.sizeID, self.rotation, self.rate, self.nInfo,) = unpack_from('xB2x4xIIIHHHHH2x', parent, offset)
        offset += 32
        self.sizes = xcb.List(parent, offset, self.nSizes, ScreenSize, 8)
        offset += len(self.sizes.buf())
        offset += xcb.type_pad(4, offset)
        self.rates = xcb.List(parent, offset, (self.nInfo - self.nSizes), RefreshRates, -1)

class GetScreenSizeRangeCookie(xcb.Cookie):
    pass

class GetScreenSizeRangeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.min_width, self.min_height, self.max_width, self.max_height,) = unpack_from('xx2x4xHHHH16x', parent, offset)

class ModeFlag:
    HsyncPositive = 1
    HsyncNegative = 2
    VsyncPositive = 4
    VsyncNegative = 8
    Interlace = 16
    DoubleScan = 32
    Csync = 64
    CsyncPositive = 128
    CsyncNegative = 256
    HskewPresent = 512
    Bcast = 1024
    PixelMultiplex = 2048
    DoubleClock = 4096
    HalveClock = 8192

class ModeInfo(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.id, self.width, self.height, self.dot_clock, self.hsync_start, self.hsync_end, self.htotal, self.hskew, self.vsync_start, self.vsync_end, self.vtotal, self.name_len, self.mode_flags,) = unpack_from('IHHIHHHHHHHHI', parent, offset)

class GetScreenResourcesCookie(xcb.Cookie):
    pass

class GetScreenResourcesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.timestamp, self.config_timestamp, self.num_crtcs, self.num_outputs, self.num_modes, self.names_len,) = unpack_from('xx2x4xIIHHHH8x', parent, offset)
        offset += 32
        self.crtcs = xcb.List(parent, offset, self.num_crtcs, 'I', 4)
        offset += len(self.crtcs.buf())
        offset += xcb.type_pad(4, offset)
        self.outputs = xcb.List(parent, offset, self.num_outputs, 'I', 4)
        offset += len(self.outputs.buf())
        offset += xcb.type_pad(32, offset)
        self.modes = xcb.List(parent, offset, self.num_modes, ModeInfo, 32)
        offset += len(self.modes.buf())
        offset += xcb.type_pad(1, offset)
        self.names = xcb.List(parent, offset, self.names_len, 'B', 1)

class Connection:
    Connected = 0
    Disconnected = 1
    Unknown = 2

class GetOutputInfoCookie(xcb.Cookie):
    pass

class GetOutputInfoReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.timestamp, self.crtc, self.mm_width, self.mm_height, self.connection, self.subpixel_order, self.num_crtcs, self.num_modes, self.num_preferred, self.num_clones, self.name_len,) = unpack_from('xB2x4xIIIIBBHHHHH', parent, offset)
        offset += 36
        self.crtcs = xcb.List(parent, offset, self.num_crtcs, 'I', 4)
        offset += len(self.crtcs.buf())
        offset += xcb.type_pad(4, offset)
        self.modes = xcb.List(parent, offset, self.num_modes, 'I', 4)
        offset += len(self.modes.buf())
        offset += xcb.type_pad(4, offset)
        self.clones = xcb.List(parent, offset, self.num_clones, 'I', 4)
        offset += len(self.clones.buf())
        offset += xcb.type_pad(1, offset)
        self.name = xcb.List(parent, offset, self.name_len, 'B', 1)

class ListOutputPropertiesCookie(xcb.Cookie):
    pass

class ListOutputPropertiesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_atoms,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.atoms = xcb.List(parent, offset, self.num_atoms, 'I', 4)

class QueryOutputPropertyCookie(xcb.Cookie):
    pass

class QueryOutputPropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.pending, self.range, self.immutable,) = unpack_from('xx2x4xBBB21x', parent, offset)
        offset += 32
        self.validValues = xcb.List(parent, offset, self.length, 'i', 4)

class GetOutputPropertyCookie(xcb.Cookie):
    pass

class GetOutputPropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.format, self.type, self.bytes_after, self.num_items,) = unpack_from('xB2x4xIII12x', parent, offset)
        offset += 32
        self.data = xcb.List(parent, offset, (self.num_items * (self.format / 8)), 'B', 1)

class CreateModeCookie(xcb.Cookie):
    pass

class CreateModeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.mode,) = unpack_from('xx2x4xI20x', parent, offset)

class GetCrtcInfoCookie(xcb.Cookie):
    pass

class GetCrtcInfoReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.timestamp, self.x, self.y, self.width, self.height, self.mode, self.rotation, self.rotations, self.num_outputs, self.num_possible_outputs,) = unpack_from('xB2x4xIhhHHIHHHH', parent, offset)
        offset += 32
        self.outputs = xcb.List(parent, offset, self.num_outputs, 'I', 4)
        offset += len(self.outputs.buf())
        offset += xcb.type_pad(4, offset)
        self.possible = xcb.List(parent, offset, self.num_possible_outputs, 'I', 4)

class SetCrtcConfigCookie(xcb.Cookie):
    pass

class SetCrtcConfigReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.timestamp,) = unpack_from('xB2x4xI20x', parent, offset)

class GetCrtcGammaSizeCookie(xcb.Cookie):
    pass

class GetCrtcGammaSizeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.size,) = unpack_from('xx2x4xH22x', parent, offset)

class GetCrtcGammaCookie(xcb.Cookie):
    pass

class GetCrtcGammaReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.size,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.red = xcb.List(parent, offset, self.size, 'H', 2)
        offset += len(self.red.buf())
        offset += xcb.type_pad(2, offset)
        self.green = xcb.List(parent, offset, self.size, 'H', 2)
        offset += len(self.green.buf())
        offset += xcb.type_pad(2, offset)
        self.blue = xcb.List(parent, offset, self.size, 'H', 2)

class GetScreenResourcesCurrentCookie(xcb.Cookie):
    pass

class GetScreenResourcesCurrentReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.timestamp, self.config_timestamp, self.num_crtcs, self.num_outputs, self.num_modes, self.names_len,) = unpack_from('xx2x4xIIHHHH8x', parent, offset)
        offset += 32
        self.crtcs = xcb.List(parent, offset, self.num_crtcs, 'I', 4)
        offset += len(self.crtcs.buf())
        offset += xcb.type_pad(4, offset)
        self.outputs = xcb.List(parent, offset, self.num_outputs, 'I', 4)
        offset += len(self.outputs.buf())
        offset += xcb.type_pad(32, offset)
        self.modes = xcb.List(parent, offset, self.num_modes, ModeInfo, 32)
        offset += len(self.modes.buf())
        offset += xcb.type_pad(1, offset)
        self.names = xcb.List(parent, offset, self.names_len, 'B', 1)

class Transform:
    Unit = 1
    ScaleUp = 2
    ScaleDown = 4
    Projective = 8

class GetCrtcTransformCookie(xcb.Cookie):
    pass

class GetCrtcTransformReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        offset += 8
        self.pending_transform = TRANSFORM(parent, offset, 36)
        offset += 36
        (self.has_transforms,) = unpack_from('B3x', parent, offset)
        offset += 4
        offset += xcb.type_pad(36, offset)
        self.current_transform = TRANSFORM(parent, offset, 36)
        offset += 36
        (self.pending_len, self.pending_nparams, self.current_len, self.current_nparams,) = unpack_from('4xHHHH', parent, offset)
        offset += 12
        offset += xcb.type_pad(1, offset)
        self.pending_filter_name = xcb.List(parent, offset, self.pending_len, 'b', 1)
        offset += len(self.pending_filter_name.buf())
        offset += xcb.type_pad(4, offset)
        self.pending_params = xcb.List(parent, offset, self.pending_nparams, 'i', 4)
        offset += len(self.pending_params.buf())
        offset += xcb.type_pad(1, offset)
        self.current_filter_name = xcb.List(parent, offset, self.current_len, 'b', 1)
        offset += len(self.current_filter_name.buf())
        offset += xcb.type_pad(4, offset)
        self.current_params = xcb.List(parent, offset, self.current_nparams, 'i', 4)

class GetPanningCookie(xcb.Cookie):
    pass

class GetPanningReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.timestamp, self.left, self.top, self.width, self.height, self.track_left, self.track_top, self.track_width, self.track_height, self.border_left, self.border_top, self.border_right, self.border_bottom,) = unpack_from('xB2x4xIHHHHHHHHhhhh', parent, offset)

class SetPanningCookie(xcb.Cookie):
    pass

class SetPanningReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.timestamp,) = unpack_from('xB2x4xI', parent, offset)

class GetOutputPrimaryCookie(xcb.Cookie):
    pass

class GetOutputPrimaryReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.output,) = unpack_from('xx2x4xI', parent, offset)

class GetProvidersCookie(xcb.Cookie):
    pass

class GetProvidersReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.timestamp, self.num_providers,) = unpack_from('xx2x4xIH18x', parent, offset)
        offset += 32
        self.providers = xcb.List(parent, offset, self.num_providers, 'I', 4)

class ProviderCapability:
    SourceOutput = 1
    SinkOutput = 2
    SourceOffload = 4
    SinkOffload = 8

class GetProviderInfoCookie(xcb.Cookie):
    pass

class GetProviderInfoReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status, self.timestamp, self.capabilities, self.num_crtcs, self.num_outputs, self.num_associated_providers, self.name_len,) = unpack_from('xB2x4xIIHHHH8x', parent, offset)
        offset += 32
        self.crtcs = xcb.List(parent, offset, self.num_crtcs, 'I', 4)
        offset += len(self.crtcs.buf())
        offset += xcb.type_pad(4, offset)
        self.outputs = xcb.List(parent, offset, self.num_outputs, 'I', 4)
        offset += len(self.outputs.buf())
        offset += xcb.type_pad(4, offset)
        self.associated_providers = xcb.List(parent, offset, self.num_associated_providers, 'I', 4)
        offset += len(self.associated_providers.buf())
        offset += xcb.type_pad(4, offset)
        self.associated_capability = xcb.List(parent, offset, self.num_associated_providers, 'I', 4)
        offset += len(self.associated_capability.buf())
        offset += xcb.type_pad(1, offset)
        self.name = xcb.List(parent, offset, self.name_len, 'b', 1)

class ListProviderPropertiesCookie(xcb.Cookie):
    pass

class ListProviderPropertiesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_atoms,) = unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.atoms = xcb.List(parent, offset, self.num_atoms, 'I', 4)

class QueryProviderPropertyCookie(xcb.Cookie):
    pass

class QueryProviderPropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.pending, self.range, self.immutable,) = unpack_from('xx2x4xBBB21x', parent, offset)
        offset += 32
        self.valid_values = xcb.List(parent, offset, self.length, 'i', 4)

class GetProviderPropertyCookie(xcb.Cookie):
    pass

class GetProviderPropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.format, self.type, self.bytes_after, self.num_items,) = unpack_from('xB2x4xIII12x', parent, offset)
        offset += 32
        self.data = xcb.List(parent, offset, (self.num_items * (self.format / 8)), 'B', 1)

class ScreenChangeNotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.rotation, self.timestamp, self.config_timestamp, self.root, self.request_window, self.sizeID, self.subpixel_order, self.width, self.height, self.mwidth, self.mheight,) = unpack_from('xB2xIIIIHHHHHH', parent, offset)

class Notify:
    CrtcChange = 0
    OutputChange = 1
    OutputProperty = 2
    ProviderChange = 3
    ProviderProperty = 4
    ResourceChange = 5

class CrtcChange(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.timestamp, self.window, self.crtc, self.mode, self.rotation, self.x, self.y, self.width, self.height,) = unpack_from('IIIIH2xhhHH', parent, offset)

class OutputChange(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.timestamp, self.config_timestamp, self.window, self.output, self.crtc, self.mode, self.rotation, self.connection, self.subpixel_order,) = unpack_from('IIIIIIHBB', parent, offset)

class OutputProperty(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.window, self.output, self.atom, self.timestamp, self.status,) = unpack_from('IIIIB11x', parent, offset)

class ProviderChange(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.timestamp, self.window, self.provider,) = unpack_from('III16x', parent, offset)

class ProviderProperty(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.window, self.provider, self.atom, self.timestamp, self.state,) = unpack_from('IIIIB11x', parent, offset)

class ResourceChange(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.timestamp, self.window,) = unpack_from('II20x', parent, offset)

class NotifyData(xcb.Union):
    def __init__(self, parent, offset, size):
        xcb.Union.__init__(self, parent, offset, size)
        self.cc = CrtcChange(parent, offset, 28)
        self.oc = OutputChange(parent, offset, 28)
        self.op = OutputProperty(parent, offset, 28)
        self.pc = ProviderChange(parent, offset, 28)
        self.pp = ProviderProperty(parent, offset, 28)
        self.rc = ResourceChange(parent, offset, 28)

class NotifyEvent(xcb.Event):
    def __init__(self, parent, offset=0):
        xcb.Event.__init__(self, parent, offset)
        (self.subCode,) = unpack_from('xB2x', parent, offset)
        offset += 4
        self.u = NotifyData(parent, offset, 168)

class randrExtension(xcb.Extension):

    def QueryVersion(self, major_version, minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', major_version, minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryVersionUnchecked(self, major_version, minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', major_version, minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def SetScreenConfig(self, window, timestamp, config_timestamp, sizeID, rotation, rate):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIHHH2x', window, timestamp, config_timestamp, sizeID, rotation, rate))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, True),
                                 SetScreenConfigCookie(),
                                 SetScreenConfigReply)

    def SetScreenConfigUnchecked(self, window, timestamp, config_timestamp, sizeID, rotation, rate):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIHHH2x', window, timestamp, config_timestamp, sizeID, rotation, rate))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, False),
                                 SetScreenConfigCookie(),
                                 SetScreenConfigReply)

    def SelectInputChecked(self, window, enable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, enable))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def SelectInput(self, window, enable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', window, enable))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def GetScreenInfo(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, True),
                                 GetScreenInfoCookie(),
                                 GetScreenInfoReply)

    def GetScreenInfoUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, False),
                                 GetScreenInfoCookie(),
                                 GetScreenInfoReply)

    def GetScreenSizeRange(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 6, False, True),
                                 GetScreenSizeRangeCookie(),
                                 GetScreenSizeRangeReply)

    def GetScreenSizeRangeUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 6, False, False),
                                 GetScreenSizeRangeCookie(),
                                 GetScreenSizeRangeReply)

    def SetScreenSizeChecked(self, window, width, height, mm_width, mm_height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHHII', window, width, height, mm_width, mm_height))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, True),
                                 xcb.VoidCookie())

    def SetScreenSize(self, window, width, height, mm_width, mm_height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIHHII', window, width, height, mm_width, mm_height))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, False),
                                 xcb.VoidCookie())

    def GetScreenResources(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 8, False, True),
                                 GetScreenResourcesCookie(),
                                 GetScreenResourcesReply)

    def GetScreenResourcesUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 8, False, False),
                                 GetScreenResourcesCookie(),
                                 GetScreenResourcesReply)

    def GetOutputInfo(self, output, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 9, False, True),
                                 GetOutputInfoCookie(),
                                 GetOutputInfoReply)

    def GetOutputInfoUnchecked(self, output, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 9, False, False),
                                 GetOutputInfoCookie(),
                                 GetOutputInfoReply)

    def ListOutputProperties(self, output):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', output))
        return self.send_request(xcb.Request(buf.getvalue(), 10, False, True),
                                 ListOutputPropertiesCookie(),
                                 ListOutputPropertiesReply)

    def ListOutputPropertiesUnchecked(self, output):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', output))
        return self.send_request(xcb.Request(buf.getvalue(), 10, False, False),
                                 ListOutputPropertiesCookie(),
                                 ListOutputPropertiesReply)

    def QueryOutputProperty(self, output, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, property))
        return self.send_request(xcb.Request(buf.getvalue(), 11, False, True),
                                 QueryOutputPropertyCookie(),
                                 QueryOutputPropertyReply)

    def QueryOutputPropertyUnchecked(self, output, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, property))
        return self.send_request(xcb.Request(buf.getvalue(), 11, False, False),
                                 QueryOutputPropertyCookie(),
                                 QueryOutputPropertyReply)

    def ConfigureOutputPropertyChecked(self, output, property, pending, range, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBB2x', output, property, pending, range))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, True),
                                 xcb.VoidCookie())

    def ConfigureOutputProperty(self, output, property, pending, range, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBB2x', output, property, pending, range))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, False),
                                 xcb.VoidCookie())

    def ChangeOutputPropertyChecked(self, output, property, type, format, mode, num_units, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIBB2xI', output, property, type, format, mode, num_units))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, True),
                                 xcb.VoidCookie())

    def ChangeOutputProperty(self, output, property, type, format, mode, num_units, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIBB2xI', output, property, type, format, mode, num_units))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, False),
                                 xcb.VoidCookie())

    def DeleteOutputPropertyChecked(self, output, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, property))
        return self.send_request(xcb.Request(buf.getvalue(), 14, True, True),
                                 xcb.VoidCookie())

    def DeleteOutputProperty(self, output, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, property))
        return self.send_request(xcb.Request(buf.getvalue(), 14, True, False),
                                 xcb.VoidCookie())

    def GetOutputProperty(self, output, property, type, long_offset, long_length, delete, pending):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIIBB2x', output, property, type, long_offset, long_length, delete, pending))
        return self.send_request(xcb.Request(buf.getvalue(), 15, False, True),
                                 GetOutputPropertyCookie(),
                                 GetOutputPropertyReply)

    def GetOutputPropertyUnchecked(self, output, property, type, long_offset, long_length, delete, pending):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIIBB2x', output, property, type, long_offset, long_length, delete, pending))
        return self.send_request(xcb.Request(buf.getvalue(), 15, False, False),
                                 GetOutputPropertyCookie(),
                                 GetOutputPropertyReply)

    def CreateMode(self, window, mode_info, name_len, name):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        for elt in xcb.Iterator(mode_info, 13, 'mode_info', False):
            buf.write(pack('=IHHIHHHHHHHHI', *elt))
        buf.write(str(buffer(array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 16, False, True),
                                 CreateModeCookie(),
                                 CreateModeReply)

    def CreateModeUnchecked(self, window, mode_info, name_len, name):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        for elt in xcb.Iterator(mode_info, 13, 'mode_info', False):
            buf.write(pack('=IHHIHHHHHHHHI', *elt))
        buf.write(str(buffer(array('b', name))))
        return self.send_request(xcb.Request(buf.getvalue(), 16, False, False),
                                 CreateModeCookie(),
                                 CreateModeReply)

    def DestroyModeChecked(self, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, True),
                                 xcb.VoidCookie())

    def DestroyMode(self, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', mode))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, False),
                                 xcb.VoidCookie())

    def AddOutputModeChecked(self, output, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, mode))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, True),
                                 xcb.VoidCookie())

    def AddOutputMode(self, output, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, mode))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, False),
                                 xcb.VoidCookie())

    def DeleteOutputModeChecked(self, output, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, mode))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def DeleteOutputMode(self, output, mode):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', output, mode))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

    def GetCrtcInfo(self, crtc, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', crtc, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 20, False, True),
                                 GetCrtcInfoCookie(),
                                 GetCrtcInfoReply)

    def GetCrtcInfoUnchecked(self, crtc, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', crtc, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 20, False, False),
                                 GetCrtcInfoCookie(),
                                 GetCrtcInfoReply)

    def SetCrtcConfig(self, crtc, timestamp, config_timestamp, x, y, mode, rotation, outputs_len, outputs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhIH2x', crtc, timestamp, config_timestamp, x, y, mode, rotation))
        buf.write(str(buffer(array('I', outputs))))
        return self.send_request(xcb.Request(buf.getvalue(), 21, False, True),
                                 SetCrtcConfigCookie(),
                                 SetCrtcConfigReply)

    def SetCrtcConfigUnchecked(self, crtc, timestamp, config_timestamp, x, y, mode, rotation, outputs_len, outputs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIhhIH2x', crtc, timestamp, config_timestamp, x, y, mode, rotation))
        buf.write(str(buffer(array('I', outputs))))
        return self.send_request(xcb.Request(buf.getvalue(), 21, False, False),
                                 SetCrtcConfigCookie(),
                                 SetCrtcConfigReply)

    def GetCrtcGammaSize(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 22, False, True),
                                 GetCrtcGammaSizeCookie(),
                                 GetCrtcGammaSizeReply)

    def GetCrtcGammaSizeUnchecked(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 22, False, False),
                                 GetCrtcGammaSizeCookie(),
                                 GetCrtcGammaSizeReply)

    def GetCrtcGamma(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 23, False, True),
                                 GetCrtcGammaCookie(),
                                 GetCrtcGammaReply)

    def GetCrtcGammaUnchecked(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 23, False, False),
                                 GetCrtcGammaCookie(),
                                 GetCrtcGammaReply)

    def SetCrtcGammaChecked(self, crtc, size, red, green, blue):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', crtc, size))
        buf.write(str(buffer(array('H', red))))
        buf.write(str(buffer(array('H', green))))
        buf.write(str(buffer(array('H', blue))))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, True),
                                 xcb.VoidCookie())

    def SetCrtcGamma(self, crtc, size, red, green, blue):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', crtc, size))
        buf.write(str(buffer(array('H', red))))
        buf.write(str(buffer(array('H', green))))
        buf.write(str(buffer(array('H', blue))))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, False),
                                 xcb.VoidCookie())

    def GetScreenResourcesCurrent(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 25, False, True),
                                 GetScreenResourcesCurrentCookie(),
                                 GetScreenResourcesCurrentReply)

    def GetScreenResourcesCurrentUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 25, False, False),
                                 GetScreenResourcesCurrentCookie(),
                                 GetScreenResourcesCurrentReply)

    def SetCrtcTransformChecked(self, crtc, transform, filter_len, filter_name, filter_params_len, filter_params):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        for elt in xcb.Iterator(transform, 9, 'transform', False):
            buf.write(pack('=iiiiiiiii', *elt))
        buf.write(pack('=H2x', filter_len))
        buf.write(str(buffer(array('b', filter_name))))
        buf.write(str(buffer(array('i', filter_params))))
        return self.send_request(xcb.Request(buf.getvalue(), 26, True, True),
                                 xcb.VoidCookie())

    def SetCrtcTransform(self, crtc, transform, filter_len, filter_name, filter_params_len, filter_params):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        for elt in xcb.Iterator(transform, 9, 'transform', False):
            buf.write(pack('=iiiiiiiii', *elt))
        buf.write(pack('=H2x', filter_len))
        buf.write(str(buffer(array('b', filter_name))))
        buf.write(str(buffer(array('i', filter_params))))
        return self.send_request(xcb.Request(buf.getvalue(), 26, True, False),
                                 xcb.VoidCookie())

    def GetCrtcTransform(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 27, False, True),
                                 GetCrtcTransformCookie(),
                                 GetCrtcTransformReply)

    def GetCrtcTransformUnchecked(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 27, False, False),
                                 GetCrtcTransformCookie(),
                                 GetCrtcTransformReply)

    def GetPanning(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 28, False, True),
                                 GetPanningCookie(),
                                 GetPanningReply)

    def GetPanningUnchecked(self, crtc):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', crtc))
        return self.send_request(xcb.Request(buf.getvalue(), 28, False, False),
                                 GetPanningCookie(),
                                 GetPanningReply)

    def SetPanning(self, crtc, timestamp, left, top, width, height, track_left, track_top, track_width, track_height, border_left, border_top, border_right, border_bottom):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHHHHHHHhhhh', crtc, timestamp, left, top, width, height, track_left, track_top, track_width, track_height, border_left, border_top, border_right, border_bottom))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, True),
                                 SetPanningCookie(),
                                 SetPanningReply)

    def SetPanningUnchecked(self, crtc, timestamp, left, top, width, height, track_left, track_top, track_width, track_height, border_left, border_top, border_right, border_bottom):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHHHHHHHHhhhh', crtc, timestamp, left, top, width, height, track_left, track_top, track_width, track_height, border_left, border_top, border_right, border_bottom))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, False),
                                 SetPanningCookie(),
                                 SetPanningReply)

    def SetOutputPrimaryChecked(self, window, output):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', window, output))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, True),
                                 xcb.VoidCookie())

    def SetOutputPrimary(self, window, output):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', window, output))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, False),
                                 xcb.VoidCookie())

    def GetOutputPrimary(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 31, False, True),
                                 GetOutputPrimaryCookie(),
                                 GetOutputPrimaryReply)

    def GetOutputPrimaryUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 31, False, False),
                                 GetOutputPrimaryCookie(),
                                 GetOutputPrimaryReply)

    def GetProviders(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 32, False, True),
                                 GetProvidersCookie(),
                                 GetProvidersReply)

    def GetProvidersUnchecked(self, window):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', window))
        return self.send_request(xcb.Request(buf.getvalue(), 32, False, False),
                                 GetProvidersCookie(),
                                 GetProvidersReply)

    def GetProviderInfo(self, provider, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', provider, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 33, False, True),
                                 GetProviderInfoCookie(),
                                 GetProviderInfoReply)

    def GetProviderInfoUnchecked(self, provider, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', provider, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 33, False, False),
                                 GetProviderInfoCookie(),
                                 GetProviderInfoReply)

    def SetProviderOffloadSinkChecked(self, provider, sink_provider, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIII', provider, sink_provider, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, True),
                                 xcb.VoidCookie())

    def SetProviderOffloadSink(self, provider, sink_provider, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIII', provider, sink_provider, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, False),
                                 xcb.VoidCookie())

    def SetProviderOutputSourceChecked(self, provider, source_provider, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIII', provider, source_provider, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, True),
                                 xcb.VoidCookie())

    def SetProviderOutputSource(self, provider, source_provider, config_timestamp):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIII', provider, source_provider, config_timestamp))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, False),
                                 xcb.VoidCookie())

    def ListProviderProperties(self, provider):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', provider))
        return self.send_request(xcb.Request(buf.getvalue(), 36, False, True),
                                 ListProviderPropertiesCookie(),
                                 ListProviderPropertiesReply)

    def ListProviderPropertiesUnchecked(self, provider):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', provider))
        return self.send_request(xcb.Request(buf.getvalue(), 36, False, False),
                                 ListProviderPropertiesCookie(),
                                 ListProviderPropertiesReply)

    def QueryProviderProperty(self, provider, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', provider, property))
        return self.send_request(xcb.Request(buf.getvalue(), 37, False, True),
                                 QueryProviderPropertyCookie(),
                                 QueryProviderPropertyReply)

    def QueryProviderPropertyUnchecked(self, provider, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', provider, property))
        return self.send_request(xcb.Request(buf.getvalue(), 37, False, False),
                                 QueryProviderPropertyCookie(),
                                 QueryProviderPropertyReply)

    def ConfigureProviderPropertyChecked(self, provider, property, pending, range, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBB2x', provider, property, pending, range))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 38, True, True),
                                 xcb.VoidCookie())

    def ConfigureProviderProperty(self, provider, property, pending, range, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIBB2x', provider, property, pending, range))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 38, True, False),
                                 xcb.VoidCookie())

    def ChangeProviderPropertyChecked(self, provider, property, type, format, mode, num_items, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIBB2xI', provider, property, type, format, mode, num_items))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 39, True, True),
                                 xcb.VoidCookie())

    def ChangeProviderProperty(self, provider, property, type, format, mode, num_items, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIBB2xI', provider, property, type, format, mode, num_items))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 39, True, False),
                                 xcb.VoidCookie())

    def DeleteProviderPropertyChecked(self, provider, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', provider, property))
        return self.send_request(xcb.Request(buf.getvalue(), 40, True, True),
                                 xcb.VoidCookie())

    def DeleteProviderProperty(self, provider, property):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', provider, property))
        return self.send_request(xcb.Request(buf.getvalue(), 40, True, False),
                                 xcb.VoidCookie())

    def GetProviderProperty(self, provider, property, type, long_offset, long_length, delete, pending):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIIBB2x', provider, property, type, long_offset, long_length, delete, pending))
        return self.send_request(xcb.Request(buf.getvalue(), 41, False, True),
                                 GetProviderPropertyCookie(),
                                 GetProviderPropertyReply)

    def GetProviderPropertyUnchecked(self, provider, property, type, long_offset, long_length, delete, pending):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIIIIBB2x', provider, property, type, long_offset, long_length, delete, pending))
        return self.send_request(xcb.Request(buf.getvalue(), 41, False, False),
                                 GetProviderPropertyCookie(),
                                 GetProviderPropertyReply)

_events = {
    0 : ScreenChangeNotifyEvent,
    1 : NotifyEvent,
}

_errors = {
    0 : (OutputError, BadOutput),
    1 : (CrtcError, BadCrtc),
    2 : (ModeError, BadMode),
    3 : (ProviderError, BadProvider),
}

xcb._add_ext(key, randrExtension, _events, _errors)
