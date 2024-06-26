# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/unit/mass/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.381480 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.mass.Scalar
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
                 kilogram: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.mass.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param kilogram: saturated float32 kilogram
        """
        self._kilogram: float

        self.kilogram = kilogram if kilogram is not None else 0.0  # type: ignore

    @property
    def kilogram(self) -> float:
        """
        saturated float32 kilogram
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kilogram

    @kilogram.setter
    def kilogram(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kilogram = x
        else:
            raise ValueError(f'kilogram: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.kilogram):
            if self.kilogram > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kilogram < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kilogram)
        else:
            _ser_.add_aligned_f32(self.kilogram)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.mass.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "kilogram"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            kilogram=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.mass.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'kilogram=%s' % self.kilogram,
        ])
        return f'uavcan.si.unit.mass.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YWO-~d-5FO-GPzix}(1V;1FQfhiP4+UfZp3&qo$Bdkr(@4_r$08kCM0r@i0MQV%Ae-%!D@DK5yM=jdaCMmy?SrH'
        'EdBbuSX@5oiJb^9bjiGQ3bgtRT+5QxrnSbaATixP3@+9oI{AKLC7$E66FkQKw9GnaDgP+KsD`fes*IfqWeeVyhc#$$nAX@xI<HKJ'
        'O_5eV%;Iyb7OLVDPcUsT2*D{HgY@_jZ=2_D5vJvyl3L8?SZ4wPu#ktlt=&4+s-Q+xakr-pgny}QFs=gAvKxj5t6hSu!3WkFA+gy>'
        '4+mH6xvhLnxr3Y{8pT(9hiQlT0G$9Qt^<7|oEC<(lPL1VM-J*h^gXSmH;W15`&M!NxwyC}s)bX6jl5Y-YoC-hLkBIUB_>Rbsh|X;'
        '?Q45ud@|MI7@NIj%M%|Vt&=qbDex>kU`J{!1+&HlrUdrW7V{>$T2ewwW`U+ntNEoBr%4AS{dkbSp3`;~p3~ip$y(pBiVADf1!pwT'
        'kmDd-2NXWGk!w{mCx=nzd*`YU-<7FH2*4A-QuYbGvQsc^PQ6mTEMJsaI}CZH+pGaklR4RiEaphn63?2a%|7jcYwFv(l6t;!DhxNz'
        'nC`t&;mzgwkd8Ca(;_n#)9!5`e$sM7glLij*%~rZmg}vR4uWxW>#VT4QDn!amo^6=gzAR>6*X1P_M;}6lbcyW7=exwf8c(#`_ps!'
        'XY3RRtF_39ZmYWNN(x|{gVpRz+H&q*XL4+zyZo*Ck$WC_`3LzPX;a_>000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
