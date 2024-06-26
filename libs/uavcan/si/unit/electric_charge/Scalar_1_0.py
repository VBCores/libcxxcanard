# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/unit/electric_charge/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.312184 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.electric_charge.Scalar
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
class Scalar_1_0:
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
                 coulomb: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.electric_charge.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param coulomb: saturated float32 coulomb
        """
        self._coulomb: float

        self.coulomb = coulomb if coulomb is not None else 0.0  # type: ignore

    @property
    def coulomb(self) -> float:
        """
        saturated float32 coulomb
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._coulomb

    @coulomb.setter
    def coulomb(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._coulomb = x
        else:
            raise ValueError(f'coulomb: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.coulomb):
            if self.coulomb > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.coulomb < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.coulomb)
        else:
            _ser_.add_aligned_f32(self.coulomb)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.electric_charge.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "coulomb"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            coulomb=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.electric_charge.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'coulomb=%s' % self.coulomb,
        ])
        return f'uavcan.si.unit.electric_charge.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YWOHUL*5FX^QJXAs;UOdP}#LK9EL6g0V;6{u$)9FXC(@D?tq#v7I6B0Q{#B`zw<)8FVtko>Ih+!^M-PQGVef53)'
        'W$D-N#p3cyPr8Zn%9PB5)7<FKTo@>sv`uHd4uI*wQE*X)=-|Vo1H8cJr+9+<X_>XWq5RXxN0PUt*JW&VD8YaXPD>_h?uJkvNp85q'
        'w8}={ytXaYMe2RLiZ8HQsERW@#k9eAph6J?c>IKSwf6TArsci{qvkEGGsOdEA@_M#dFOPagC5a|wZ5@D{L5;C2_2Y$b{J}`b_r5)'
        'A6R1*V7-$b4X(>`S^0)?2RTJFim&({(+=~2w~9M;6X+Y^G<-<oi7H=w?6?d>-_uz7S21CH-zsi?)9JLR7S0GZih4Qqq>aWl0@D&x'
        'R$?k>pQr5`V`E}6Q{@Efy?V<N9R-~O$pa`nPY>C#9)n_?b%AMxhiQv>8=VA77+@WzW>YW!jHZj$24sTqAn#t#a28(B-L=iC-|IBy'
        'j@sa?Ar>$W;95@M<1PwA@;ewtlkc62LUdPVZXp0q08801m^N>DhIVGIDPNT@%d8@XJlt(ob5Bh=XhW8Dq$S{a{jA=nkqATZd)K1R'
        'hffE??KP(RuXT8Pxjv%hmHcUu*$&h0T_Aqa2us|klLKfhSt<+nt^>z|b#oJ~5D!hptovzmz?IVN@V`TKm9vM@5Y5T$EFp}ziGV+F'
        'zuNuj1-+hb287jW6hybtZT2Sxe4K+`_9zWJSFbY|cf7rPV24q75k>h2xEbzE^#cF^'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
