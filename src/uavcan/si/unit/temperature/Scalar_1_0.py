# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/unit/temperature/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.387363 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.temperature.Scalar
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
                 kelvin: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.temperature.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param kelvin: saturated float32 kelvin
        """
        self._kelvin: float

        self.kelvin = kelvin if kelvin is not None else 0.0  # type: ignore

    @property
    def kelvin(self) -> float:
        """
        saturated float32 kelvin
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kelvin

    @kelvin.setter
    def kelvin(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kelvin = x
        else:
            raise ValueError(f'kelvin: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.kelvin):
            if self.kelvin > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kelvin < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kelvin)
        else:
            _ser_.add_aligned_f32(self.kelvin)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.temperature.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "kelvin"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            kelvin=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.temperature.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'kelvin=%s' % self.kelvin,
        ])
        return f'uavcan.si.unit.temperature.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YWO-~d-5FO-GPzix}@gQChFQfhiP4+T^8!_HYr+d2C>DV*f>5t8>35gseVmi@;@(21$uzDBV6~kPndaCMmy?SrH'
        'EdBbuSWKSu*p8)_x?~=l;#z&?LPN=F(^}(I08ICff{S&C4&IL~-~~QA#S`35%dF!q<)1`8ta(>@RmM(*GC*s=@!U`z)m(FjX^joR'
        'd1X3minRLSD!#yKp(@Vs6w?OdAvh&s0FNK>wz2*eVOs7f&~i4;I+Hwb7V?a@wOglJ71WR_?)J3d;a^4@OsK##bc4`fwM&pS_kp!W'
        '0yaD8VgI^4x0SCccaT#=qxg#NFzqlOcqh4&^FZGSr{x1$O_cfKW5?@2^gXSmcNG)H_pM_7xxBnAs)aLxjiOmjE1y6QRflPbNmFAg'
        '=rd2-b6aC#JQd^wo4sbs6B`NELCph5JWmhUu^NG7*0{iw#KW}3yos&`N@!q~)2wMVzqArGXP@*R_4C&Y+Regqy1Ox1@H<vfVQsqL'
        'j3yE=3g9|U;UgP`RyA`lh&tap(}dWrOpQVSo&c7zSxERfyI|U!8m4?%z9_SR81i1XS;IXI=%5Q((V?mV&zq;sKCMG&g5JB<d$xBf'
        '3^&i1?!8js&E$MU$1CO2A~P1#?rk7`+zLayXp#eH4Y?_6_I5J1aWns{u)0y?$)=Y!`&>%Z4gM=?s+>KHnrM!1W(i@)bp-r@`_=AG'
        'FX+dyQy{F?q9D30nSiWG0UzaHHQSSxox9f=j4baa|JGp?UPMv;0Z0DRAM67F00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
