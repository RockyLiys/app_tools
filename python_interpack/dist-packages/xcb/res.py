#
# This file generated automatically from res.xml by py_client.py.
# Edit at your peril.
#

import xcb
import cStringIO
from struct import pack, unpack_from
from array import array
import xproto

MAJOR_VERSION = 1
MINOR_VERSION = 2

key = xcb.ExtensionKey('X-Resource')

class Client(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.resource_base, self.resource_mask,) = unpack_from('II', parent, offset)

class Type(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.resource_type, self.count,) = unpack_from('II', parent, offset)

class ClientIdMask:
    ClientXID = 1
    LocalClientPID = 2

class ClientIdSpec(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.client, self.mask,) = unpack_from('II', parent, offset)

class ClientIdValue(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        self.spec = ClientIdSpec(parent, offset, 8)
        offset += 8
        (self.length,) = unpack_from('I', parent, offset)
        offset += 4
        offset += xcb.type_pad(4, offset)
        self.value = xcb.List(parent, offset, self.length, 'I', 4)
        offset += len(self.value.buf())
        xcb._resize_obj(self, offset - base)

class ResourceIdSpec(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.resource, self.type,) = unpack_from('II', parent, offset)

class ResourceSizeSpec(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.spec = ResourceIdSpec(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(4, offset)
        (self.bytes, self.ref_count, self.use_count,) = unpack_from('III', parent, offset)

class ResourceSizeValue(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        self.size = ResourceSizeSpec(parent, offset, 20)
        offset += 20
        (self.num_cross_references,) = unpack_from('I', parent, offset)
        offset += 4
        offset += xcb.type_pad(20, offset)
        self.cross_references = xcb.List(parent, offset, self.num_cross_references, ResourceSizeSpec, 20)
        offset += len(self.cross_references.buf())
        xcb._resize_obj(self, offset - base)

class QueryVersionCookie(xcb.Cookie):
    pass

class QueryVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.server_major, self.server_minor,) = unpack_from('xx2x4xHH', parent, offset)

class QueryClientsCookie(xcb.Cookie):
    pass

class QueryClientsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_clients,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.clients = xcb.List(parent, offset, self.num_clients, Client, 8)

class QueryClientResourcesCookie(xcb.Cookie):
    pass

class QueryClientResourcesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_types,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.types = xcb.List(parent, offset, self.num_types, Type, 8)

class QueryClientPixmapBytesCookie(xcb.Cookie):
    pass

class QueryClientPixmapBytesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.bytes, self.bytes_overflow,) = unpack_from('xx2x4xII', parent, offset)

class QueryClientIdsCookie(xcb.Cookie):
    pass

class QueryClientIdsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_ids,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.ids = xcb.List(parent, offset, self.num_ids, ClientIdValue, -1)

class QueryResourceBytesCookie(xcb.Cookie):
    pass

class QueryResourceBytesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_sizes,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.sizes = xcb.List(parent, offset, self.num_sizes, ResourceSizeValue, -1)

class resExtension(xcb.Extension):

    def QueryVersion(self, client_major, client_minor):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB', client_major, client_minor))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryVersionUnchecked(self, client_major, client_minor):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xBB', client_major, client_minor))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryClients(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, True),
                                 QueryClientsCookie(),
                                 QueryClientsReply)

    def QueryClientsUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, False),
                                 QueryClientsCookie(),
                                 QueryClientsReply)

    def QueryClientResources(self, xid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', xid))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, True),
                                 QueryClientResourcesCookie(),
                                 QueryClientResourcesReply)

    def QueryClientResourcesUnchecked(self, xid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', xid))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, False),
                                 QueryClientResourcesCookie(),
                                 QueryClientResourcesReply)

    def QueryClientPixmapBytes(self, xid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', xid))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, True),
                                 QueryClientPixmapBytesCookie(),
                                 QueryClientPixmapBytesReply)

    def QueryClientPixmapBytesUnchecked(self, xid):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', xid))
        return self.send_request(xcb.Request(buf.getvalue(), 3, False, False),
                                 QueryClientPixmapBytesCookie(),
                                 QueryClientPixmapBytesReply)

    def QueryClientIds(self, num_specs, specs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', num_specs))
        for elt in xcb.Iterator(specs, 2, 'specs', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 4, False, True),
                                 QueryClientIdsCookie(),
                                 QueryClientIdsReply)

    def QueryClientIdsUnchecked(self, num_specs, specs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', num_specs))
        for elt in xcb.Iterator(specs, 2, 'specs', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 4, False, False),
                                 QueryClientIdsCookie(),
                                 QueryClientIdsReply)

    def QueryResourceBytes(self, client, num_specs, specs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', client, num_specs))
        for elt in xcb.Iterator(specs, 2, 'specs', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, True),
                                 QueryResourceBytesCookie(),
                                 QueryResourceBytesReply)

    def QueryResourceBytesUnchecked(self, client, num_specs, specs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', client, num_specs))
        for elt in xcb.Iterator(specs, 2, 'specs', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 5, False, False),
                                 QueryResourceBytesCookie(),
                                 QueryResourceBytesReply)

_events = {
}

_errors = {
}

xcb._add_ext(key, resExtension, _events, _errors)
