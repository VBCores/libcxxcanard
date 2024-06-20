# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/unit/force/Vector3.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.369921 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.force.Vector3
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
class Vector3_1_0:
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
    def __init__(self,
                 newton: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.unit.force.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param newton: saturated float32[3] newton
        """
        self._newton: _NDArray_[_np_.float32]

        if newton is None:
            self.newton = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(newton, _np_.ndarray) and newton.dtype == _np_.float32 and newton.ndim == 1 and newton.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._newton = newton
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                newton = _np_.array(newton, _np_.float32).flatten()
                if not newton.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'newton: invalid array length: not {newton.size} == 3')
                self._newton = newton
            assert isinstance(self._newton, _np_.ndarray)
            assert self._newton.dtype == _np_.float32  # type: ignore
            assert self._newton.ndim == 1
            assert len(self._newton) == 3

    @property
    def newton(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] newton
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton

    @newton.setter
    def newton(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._newton = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'newton: invalid array length: not {x.size} == 3')
            self._newton = x
        assert isinstance(self._newton, _np_.ndarray)
        assert self._newton.dtype == _np_.float32  # type: ignore
        assert self._newton.ndim == 1
        assert len(self._newton) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.newton) == 3, 'self.newton: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.newton)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.force.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "newton"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            newton=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.force.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'newton=%s' % _np_.array2string(self.newton, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.unit.force.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YX-%k`V5Z;61mxziOAJjyi3_iGGFd84#cqT631q^SdbhqW&*xhd0?s;oMA`cQVO~f$%y*Rx)JV0-g%XK?5-^_e7'
        '-+pcW{?&~7kH25m%rX@d%Z;Q;exa%2G0AjZYAYQFzp(90mAT6B4|U1m1Rfs1KCJjDQqUaj_bS@WXc1c(SA}%(o;DeecX;NsSpz>y'
        'y4+Z)3lNc?*%_WsAZaAgAsm38C)7D3)5>uRA7NZYf1SWjwIo+;RLK>>sH4P%^8DQ~;l|J!{H>PkakkEjjuS7#)y19`2v<Dkg&Ts6'
        'siibBmri!kW3Ht%br(_QNh%#t{UneqV|^L5j^vtg5O@6T_E~rci(jK{Bbbnr=o@Tdk;FP$FlyL&pzny2(+*Nxv5<Jr(99v17CCMW'
        '&xrA3F*^U8o}NZY;}Bu1)X!ldCC#L(A(`||k}3>-aMt4}7q;szzk|Q}O1c4a+xR-{)=v^$f?pm7V(UEBN@n1fHh8X)!BFS>k{gQq'
        'G2(2RWJ2Ol#Z!NCi<jKV|NBjlPguKnfqvIFE2XHZFFPStm#T`xPgqHok8O&bH%TrFNOr@4_QGK%%%f5i1CmDYjE*fb%zGs*`YXCw'
        'r6E*I`RRgxc6fuqOk*bza!LKtxxFQ6Jy63wh(s(}Tmi;Q!!znQgCl>9?1jA}r8bU82Ah77SY4q|(4aUeDGu1rgg+%y9Bv!M*K3E{'
        '6KuNi7;_69)HYE{bj)<&j8-^#-gDd(RE5Q_QY4xf-odso??@Fm<>`S+5x^oqGbj~>)YmHb8$-3mPvX@$%n@AJ!zCi9#o9~|1S+5_'
        '(fLTMiw*HetoFGUYvS2pGJ}z{DPywe{4+PSKF3c%IWR*qi^RT3c0~(+ZxQC*knQ*n3mi-hoCE*>'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)