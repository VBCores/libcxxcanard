# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/sensor/Status.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.515859 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.sensor.Status
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.duration
import uavcan.si.unit.temperature

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Status_0_1:
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
    MAX_PUBLICATION_PERIOD: int = 1

    def __init__(self,
                 data_validity_period: None | uavcan.si.unit.duration.Scalar_1_0 = None,
                 error_count:          None | int | _np_.uint32 = None,
                 sensor_temperature:   None | uavcan.si.unit.temperature.Scalar_1_0 = None) -> None:
        """
        reg.udral.service.sensor.Status.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param data_validity_period: uavcan.si.unit.duration.Scalar.1.0 data_validity_period
        :param error_count:          saturated uint32 error_count
        :param sensor_temperature:   uavcan.si.unit.temperature.Scalar.1.0 sensor_temperature
        """
        self._data_validity_period: uavcan.si.unit.duration.Scalar_1_0
        self._error_count:          int
        self._sensor_temperature:   uavcan.si.unit.temperature.Scalar_1_0

        if data_validity_period is None:
            self.data_validity_period = uavcan.si.unit.duration.Scalar_1_0()
        elif isinstance(data_validity_period, uavcan.si.unit.duration.Scalar_1_0):
            self.data_validity_period = data_validity_period
        else:
            raise ValueError(f'data_validity_period: expected uavcan.si.unit.duration.Scalar_1_0 '
                             f'got {type(data_validity_period).__name__}')

        self.error_count = error_count if error_count is not None else 0  # type: ignore

        if sensor_temperature is None:
            self.sensor_temperature = uavcan.si.unit.temperature.Scalar_1_0()
        elif isinstance(sensor_temperature, uavcan.si.unit.temperature.Scalar_1_0):
            self.sensor_temperature = sensor_temperature
        else:
            raise ValueError(f'sensor_temperature: expected uavcan.si.unit.temperature.Scalar_1_0 '
                             f'got {type(sensor_temperature).__name__}')

    @property
    def data_validity_period(self) -> uavcan.si.unit.duration.Scalar_1_0:
        """
        uavcan.si.unit.duration.Scalar.1.0 data_validity_period
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data_validity_period

    @data_validity_period.setter
    def data_validity_period(self, x: uavcan.si.unit.duration.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.duration.Scalar_1_0):
            self._data_validity_period = x
        else:
            raise ValueError(f'data_validity_period: expected uavcan.si.unit.duration.Scalar_1_0 got {type(x).__name__}')

    @property
    def error_count(self) -> int:
        """
        saturated uint32 error_count
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error_count

    @error_count.setter
    def error_count(self, x: int | _np_.uint32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._error_count = x
        else:
            raise ValueError(f'error_count: value {x} is not in [0, 4294967295]')

    @property
    def sensor_temperature(self) -> uavcan.si.unit.temperature.Scalar_1_0:
        """
        uavcan.si.unit.temperature.Scalar.1.0 sensor_temperature
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._sensor_temperature

    @sensor_temperature.setter
    def sensor_temperature(self, x: uavcan.si.unit.temperature.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.temperature.Scalar_1_0):
            self._sensor_temperature = x
        else:
            raise ValueError(f'sensor_temperature: expected uavcan.si.unit.temperature.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.data_validity_period._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.add_aligned_u32(max(min(self.error_count, 4294967295), 0))
        _ser_.pad_to_alignment(8)
        self.sensor_temperature._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of reg.udral.service.sensor.Status.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Status_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "data_validity_period"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.duration.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "error_count"
        _f1_ = _des_.fetch_aligned_u32()
        # Temporary _f2_ holds the value of "sensor_temperature"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.temperature.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Status_0_1(
            data_validity_period=_f0_,
            error_count=_f1_,
            sensor_temperature=_f2_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of reg.udral.service.sensor.Status.0.1'
        assert isinstance(self, Status_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'data_validity_period=%s' % self.data_validity_period,
            'error_count=%s' % self.error_count,
            'sensor_temperature=%s' % self.sensor_temperature,
        ])
        return f'reg.udral.service.sensor.Status.0.1({_o_0_})'

    _EXTENT_BYTES_ = 63

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8fDd$L0{@j(TW{P%6i#}}HtB_uHdI2;sgO!4TGNVxpaR-7NlUcNMVq9mK*b%~vwMbmZEHN<ZmL$INT3E;qM}13c;+VYjKmM('
        'nP=Y0H+D9ANur3AR<>u(oO9-!@B3!H-1oyjV?)I+Kb5QnX%ISYDwO1*e89a>IIbTzlQ@-HnEddJ2xSwm!OB`9%rkTLv3X=B^8>Do'
        'BB2Zo<%gHG%6y$E(QmTfjd&9-PASoFvOw|BL70~G1)fnFD`#1AouwwPxGkYl8AsOL$gPd{XQnz-9sb5VHu;##wN}#0v`Ebz_}(G$'
        'O)Hb{zb-`>bh8<C1FpHNZHhEf4$^4;dd6EmkDOFGStPX+WQuD<cb0t~a_sLA9jOjihin>j?2e%m8%s~_ltZFyy<`hH9K0UJT=!RH'
        '%=M&pLlHGJnJPnGK2NpVj05C#I-gkTEVs*?Y0S;rDO-%MP0i%T-Bj}^;40{K^aOsIyn!8Lfel<&+_&4X#l61q4j<nh8|wYNc=4jB'
        'aLr^MYH=VHejEiR-{%IgZ}K4w^L)Ig_O7>9HuaIAcj#1#-2@_0!sh^pS<jESb=ekyo5V`HGB6AIF*l7f<qJ%N!c91G%}4AblpgY2'
        '0?gV=cJvu)GyFDUQ*1%ACy_8jI$FgcHX+(tsEFhB)g<#m>AOHx7TUPo#$vYz%6`H@3J3daPqDhwRg)hr`|4bDE;zP(M%$u}yTnsu'
        'r$nUP4Un33x<v1y7G4OyXFAR979ECq@Z02vu1S5f_+G~6M%(kfZk(8$?c^j~YkDy@g-qr}GX|7wwu^~C+Og_oolg>|rse$T5)T3y'
        'HMSVhZ9BV=h1llW;4D0}c$f+Eotdn%r>O_-C8Z-%tz;gy+mw;TC0=;jzKmFGqS9Dht=MHlPg9^xv=bf`JYC4V)GGjVyyyf1$Uy2f'
        '7qMlGWH03pXE4E1-b_M~ve?sHMj~KbGcB8ft)vX4XT`$qpklIqnN8w(9u{ZWhip6dqqFTqDmV*@5EN%&z&ybMnff4!2pkLUP1b^9'
        '<EzNKf%tQg77d~L_(^A~jNYWT=-iWHOJhQ*SV0l9NZXzKI2ZX!G=UR@j3Zw#q`_j}&lJD|X=62kmNFf)2SUZ{K8c8F60DRwCQ~-M'
        'aAWGm?2I$If??4HIawg;5=ccgSzN~&)Bw;=HRuf1F&?oZ4ZB*}8rt{;M9zbLA`0+1u+6T*ogPp)Et&-=px3*L9KErnEOeeO?4l$0'
        'MA!m~EPtRN^d8jWD|(pH`|I?<0$rw$Ch23kLRV>uuF*8j&@5fg$9fVo^oivqRSOQ%O<F9{pc<`ig8b9Xx6jK--oZ5a7RnSLWr2Ua'
        '2e>4=XnnbCiQ5<VQvSDXOV60?NT-3I2@_@cozb~s90nG<%`DUsof$L(+EsV5*KML=552YUDHAz2YQq4^Ss~ZkHoI<lgU}J<%!;3a'
        'eM?#zA{Q*E+e42v`I@CbGj0K-G6ELC3;}t=3TB0}0Lyq@nYJL~k?z9(B*mK@uk;dOVt(qjyR>@k=G^qu%G~0DyEI#yTb!{Kt9(`-'
        '8~_f_U+ZWb1VV|_rq*{RR%*pwpyV4diPHsuuYiy3jIel_q%UZK6ovFXY5IwtXFGr=--~kqr+sn1z=_cjZ+n>8qFTi-ZW++~i(SPp'
        'kd?QmSVQ0zBmE9N)4~=ttH-KYUIai>6m~#eiZdvsQp3=S_&zI&i&K(Cv9<%~jV8W9{zUi^y$M)xnR3i-kY4T4@)PKiJz%444~6_-'
        'c_u)8?9FHwZ-16S|Jup&7PvFq&z*uYTR0|CYjhPxSGz_X-VF?|m&SK7dUvaF|8U7o8iORgWTj{lFbDyG=l>5D^fUcJztV5?dsj#P'
        'z)@ze5rF&rzr*<it}f-(R=Fg2fJb>bjQb?-Y<1Y)yGj~t+qK@BZjqwiM!r(xQA5<A*jny%zTYd4-75pKR(V<!Ca4aPK=NBPtt>H`'
        'Hh*%@_KN5H2kaSGZutuU00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
