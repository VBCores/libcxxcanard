# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/unit/force/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.366352 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.force.Scalar
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
                 newton: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.force.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param newton: saturated float32 newton
        """
        self._newton: float

        self.newton = newton if newton is not None else 0.0  # type: ignore

    @property
    def newton(self) -> float:
        """
        saturated float32 newton
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton

    @newton.setter
    def newton(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._newton = x
        else:
            raise ValueError(f'newton: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.newton):
            if self.newton > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.newton < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.newton)
        else:
            _ser_.add_aligned_f32(self.newton)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.force.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "newton"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            newton=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.force.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'newton=%s' % self.newton,
        ])
        return f'uavcan.si.unit.force.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YWO;1!Y6n)62pb`Rc!$MYwo2UK-O=j~1Ct}>0rhP5bCVg$wk8#F?L>3Y;O*G;9)BHW-?F=}G;ceb+@9pV5_ndxN'
        '`t^IUntu6-8}q<*O@i=>YW0~iEo#!*&e@=%fc)?{`qakc#rv@na0$=O;1mw>GBLEn{BEMdmYO=KIvEw~6YE=1AGcIf4|$CYg%8Ra'
        'kX2s&a1~!dv(QxMa0YpU&=|d9DT)9e;jV`M7C~O_DWUnik#)jpq$HN^?mF(g>Qq!ithnFPmd1a%Y!Id*(ZUR(gk}#RTN)ziEEgbm'
        '^5g#X@p7zwjk&{;LK@Xqcn5ihgh&mip5FxehBzG^;7}4T7oT|AMx-BbEWN83F}`nAH^0ebQZ)<b2%DH(&MQWIiddJI2)8Zd3b$$A'
        'zA-hz#xp5SLGH_~fNZ#MUbHj{4j1_mIZ-3QiL*Wu#o;J#kzf<5gb6K(qu6U+EkCUo_Sr|}NBy#UiL+UFj(1C2q`v1A7Pi(zZ#9w-'
        'qbR(g81A~nv}%bLgQUy7b4`%#%FH4N5D;Lg*aT&q8U^y^%qsQE`bAx&gIFfIO(YH2ninP(Er$wgFXU5sfP-KfLHDnfo=+SL<Lx!%'
        '2d`9oGhH9!@=Ei(NUVdrcNa()cg!Lq?Bq~%7JXFIdh3Lz(fYY_R!A!qx>5G>W}kAd%;3Kw*_7;2(nxcBJBtWIs*`{paM0}i3=E%)'
        'n*l+ymKf6QlqsgffR0MAT8xQfE~nRt7&&UDuj(kVz!Izf0LFHd$KV4100'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
