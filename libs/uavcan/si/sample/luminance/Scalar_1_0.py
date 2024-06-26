# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/luminance/Scalar.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.805669 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.luminance.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time

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
                 timestamp:                None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 candela_per_square_meter: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.luminance.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param candela_per_square_meter: saturated float32 candela_per_square_meter
        """
        self._timestamp:                uavcan.time.SynchronizedTimestamp_1_0
        self._candela_per_square_meter: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.candela_per_square_meter = candela_per_square_meter if candela_per_square_meter is not None else 0.0  # type: ignore

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def candela_per_square_meter(self) -> float:
        """
        saturated float32 candela_per_square_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._candela_per_square_meter

    @candela_per_square_meter.setter
    def candela_per_square_meter(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._candela_per_square_meter = x
        else:
            raise ValueError(f'candela_per_square_meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.candela_per_square_meter):
            if self.candela_per_square_meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.candela_per_square_meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.candela_per_square_meter)
        else:
            _ser_.add_aligned_f32(self.candela_per_square_meter)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.luminance.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "candela_per_square_meter"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            candela_per_square_meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.luminance.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'candela_per_square_meter=%s' % self.candela_per_square_meter,
        ])
        return f'uavcan.si.sample.luminance.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaZExK~7QRWF_r8U+rL<6{g>94FUIT%YEDO6pP`B*ROGR6V_NCU?p4=J5_L!M*l8dy`@&VMWEMci$iJ!nv;3pt~'
        'U_Y||0PQc}TRF!b-+NQqNXc_NGd}0cd3lcWufzYjc(hah6whXZ$V9Q{8?Ggb<tHqNx#x!}$&`_nSH;m=R_CG3HNQQ`cy+&8`Lz0H'
        'wOma3DNA7gLe6$VmU>2dh9w!i9p{NmSsHThR>)$et76vQ;o3-*R-#kPeCXu+6`i1+&#O<XV!>zDY8m8~o9Z8+{V{$GPgTX#HOb>>'
        '<j=exG0S|5PKwE9QA`cpvoZmH25Bg?O64a!x(y4)g2$DZ5p%64;s{t5C*12xkMkqbGLcs9fFDbDQX~5*kKRo!?{j@HN(+7<tsnEW'
        'Z$(Ad!OM^t>nAD#FP|<>-)t4(Yu*Oz-M}pj&1cmIRdLb>AJd5GXk5{L9>CQW5*cb`c&O5-Dh~UR3aickPj))D1t)2q1Y8rfMaE7U'
        'Vg<8AupLe^W(<#rk&q~2RKf|<U_vuJAPGFCmdF&&*C(wvk4oJ-C{<eaVS8D6+`Cer!T^(i8NNcKAraq_5EGJd-DO!8%aB>fxkpe<'
        'm}`xChOeNd-0*ow6bU%d{No&Q1Fvssm5j8TVft!iBmu{`zCsM=^`TIKUX#H^W!i^Ty(8gnwJWl=J`cA5=XO|}bM(?GlJXr46a3kV'
        ')o$b8aDVM;7eYdIWdwfmkb#e{&Ce6kC98MWt{#jm9A|;bEm>V%Un2v~w7Eidg$xC5L0_bH;E}h;)mLhrWAB3BIn<6OyDE<(Fa#C|'
        '$<vgF+!&^1JZM~iLLkzbp|=n=cn!S8jI4oGD^zaqRBax%qa0Ka2G&3^-;)rp)IuGTP)j3?*IZ^JhFXwecjK)dSx%KD*WOtnPzfo-'
        'QiHvaX()<3!+5<)f&nxsTFlrWR;<o3BnrsDs~x}Hrivu!ejg4S!QvP*jOEskdAB~^nAqZ@KqVX&ni{pkJU~%gwpbPz1C6^WB!)l`'
        'jaNY<94lrwRElk4hkYlO#Ca!OpzGqIc%F8!pTy;+b!P7LXz%@xdX-oyF8!5j^|0x>-XL!njqOzJre0M{`?W(=@k~n!d@qB7Loz!+'
        '39}#6^~vJaAF)=<!IeW?HL!op$=K%|I`KJpW`aE6#nKoL`oW-~SiHruI4fQj-5dxd;$RfoiAU9bam?S6dpz<nQNE0-Ua{yKmFtkh'
        'M$G+;0bLX`2(b*RV(uo;`rb`ky$|#>@d6NsP{`wxnS_H-k5;P~eB^sjTX=`!T$TsWz`o}FJVv`CriIH)Hv|iMFlJS8{*ff>z2v><'
        'VbCgzw6^36X23b50pB%hwGYYow%0U1S|Dfvs|I*LX<!8mHr6jRH-pBtyGn0&>&`G^HtXEgMxkP?IM8XJK*f2(1vM3n?7)MNeF41&'
        '(Nzf$UE~a7-3AIY0ZX-PT=(J*oKd=KG9Jn;Iacp5D7LwWoE*duqDyVPj3^u~Z6AKFiX(4J`(FKgiw}#rIOMCWD#+uMm_ZUK$PYyI'
        '22YeD$M>NtnN@l;il+Tg01Z^)@5S+(EJBX_)gi%fx0lB-wg(UIinTAQWx8IP00w&2XsGCH9>6_e;^TM&f$gC%gCh>A1(nhXe6Lf|'
        'Nr#6JCrf(RJx?J{lyusy&$#tjhjVUy9&x&)3-0_8#MzP_MLb;6WA6NM#D$WcaQlmhQzd=E=~+U2qNFDgPn7f&;<1vRMm$o|ClTjM'
        'dd9u~l(T!***WL*Jnif~gLtl_=Mm4A^jXBGN=gvVl=K4PlO?@~c)Fy|A)YGf^N1%)`WwWhl3sFtT}E6i>9X^01@U-Ef9w4G9pcfF'
        'UUB|*-F-dh_X~(~C4JHP{}SR%Nmt!HUUu<##oedQ>!Fffb@zJJ#dqD^@ApmK>1z)E;P7>aZ#ev;!#_EE)8Tc8n+}D;J%{%ke(CTl'
        'hhIDV#^H|+e{%S9gEwX;oN%TUmRn)H6|T3!W-EwR*lUG*t?*?leANnHx578A@MA0d)Cxa4A&0L#m<%vakmB81fCLYdXU>kkJ6DPh'
        '4zS_ZCVUXiU4xNo4}3$y1S2rPR>kFepg3WD_?XG@^YM*;FLuU%9z1y9hDmMd46t&<W9CB}`{v^u$ktCdkUAI^KftsRZ=&|^#iID1'
        '_-`)W-WMA^@s9ZOvbZkZ6@L*_yeDpmUNLE4GE6rg_b@?*pZ8U9y!pUCNbcg+J{k~r#AZVqe-n3y>=F*8yJL)V3I;e%wDghGRm?Ta'
        '1;YaWH+ZBrUu@F}xONQFK7rp9?0(mSh5i_I5uh$^@X#h4+8iC)Mi%?kGG@&C1rr0?Gc64O00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
