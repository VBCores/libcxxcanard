# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/node/port/ServiceID.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.291657 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.ServiceID
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ServiceID_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    MAX: int = 511

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.node.port.ServiceID.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint9 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint9 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 511:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 511]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 511), 0), 9)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.node.port.ServiceID.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> ServiceID_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(9)
        self = ServiceID_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.node.port.ServiceID.1.0'
        assert isinstance(self, ServiceID_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.port.ServiceID.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{?YWU27CE6y3GmcDL1P-BPfkoeD}@aMU+nwNfbK)}^f<FA_47yPLpFW=Jy2t{~V43x$9}<L}j*{cJ0pmq~K(Jvryz'
        'lOOYc<a}lL+0A0WG)qIGK?$0QZ!}IJBuSnXxfTYTy>o0-nV3?+$)Est;dV~lceib8MA8i78zt=}RE9EV5Ei*I;W4P5NZ{a|vvtw~'
        'rA00suh_*;<MoA$s!`?4ojSWrs4+^!r2*}}BJ2%>rdiI`_64MDMr4UFYA7+D-A(0%5}7cfhZ)U}Qj4wxb|4LOL0wg~Ok!b33bJds'
        'iy8=?P;E$t;v8SI>+K1UFAMiD*76}#RQc(SoLwW@P|2ubmx0d9nAdErN7E7+%oCO;&Q=_ruGsosE`5!elHg6gK3+YD8hnF4=9?pg'
        'xz?L6j&JcNc7cq+9!&&8zfhokf3L``A5nv6G@ZcnUEAm=n)p+V@%`}{<E_8dsCtGnbX>+@o0n!o;=yR%o>jnC`3`?tVz(IJtqC>2'
        '+__yL9nl9yybFk6?$E9hotG*B45UB`ioLLl{+Ei_*+v^Z)^GdM3+#RM1@?yL-c+{=fr&{jjmlFb34H^~i?9!iGEPN86m-kf-#eQ='
        's#zGB5pld7@#m>Hdw*)l@KyLS^bK>ykE=;I)yPYMG~O~k$({2p`+8jQ97}=|4uPVw3p&8efI&x~e}Z@r7>wuw644RKu+O0%Z=52P'
        'XOqFqe1JEY>w9N!zZK^FaDNO_6WBSD7tRJZf#^XN=hz37(1I*SpZnWC6riZd)y&TeB;f*I3qP`V+mtaOyZ<He&pvusrYTi}>ruY@'
        '%WX%E-#W&}T#OK0R4-%HnF;BldwxOtezEA^2~NfHU-E{ea`@g4%h)?A{0E`7HY|Ar000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
