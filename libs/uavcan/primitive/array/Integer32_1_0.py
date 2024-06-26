# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/primitive/array/Integer32.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.895908 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Integer32
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
class Integer32_1_0:
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
                 value: None | _NDArray_[_np_.int32] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Integer32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int32[<=64] value
        """
        self._value: _NDArray_[_np_.int32]

        if value is None:
            self.value = _np_.array([], _np_.int32)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.int32 and value.ndim == 1 and value.size <= 64:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.int32).flatten()
                if not value.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 64')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.int32  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 64

    @property
    def value(self) -> _NDArray_[_np_.int32]:
        """
        saturated int32[<=64] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.int32] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.int32 and x.ndim == 1 and x.size <= 64:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.int32).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 64')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.int32  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 64, 'self.value: saturated int32[<=64]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Integer32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Integer32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.int32, _len0_)
        assert len(_f0_) <= 64, 'saturated int32[<=64]'
        self = Integer32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Integer32.1.0'
        assert isinstance(self, Integer32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Integer32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{`t<TW=Fb6!zX1!Yzbbp@oG4H5AOfTzYdstx}yHN}=Vg+N|wqcGdOT+FeIUC8Y4sDo7)BB!>4q=4a$Ff1&M59`iGL'
        '#&#}lFc3(B+9ogFJ(ur%b7pq!FK5zxws5r2{^Q4*6Sb@sm;8*SQ4mMJ1eKVT{A#1#Y-CZ+B;WZUPg~Wzm9p<AnoK^GXCBK(vdAqz'
        '3F_qcTESQ~NJ`B#sz-S=#!5k&1{0;PlbnsR^vY$)U4M+FS=2~mSm4gX?)6g%8Wet$k0l@QgFH{8N-JlX{89E}wG<?|^;N{;+A^E%'
        'el5rYKUWm_kv{2)m*fW@24p46H!K;=!!MMzcWFC)7PC4_@-AK<I!h~-eDFauny^}T&An&?ekIENxLr(wM^vjpmizTajmhvZKX7jm'
        'Mx~YRkPnrM+Ee&d-j{rzpXEVP3)0$3ps7}cZzH5;P>u2l31z;w>+*k6t?5uF{GlI`tS`Cn7`UMqo&Zgi3Qs9i)33yt<fj)Gy<C*m'
        'pa1h-@*TIMywl1DblXMdhTmw?;phjFP1GxmII2oMgsk46mgaOOzHPEJ$Q$W$^K8EwMzqo4HNO8&BdG>COP(95nxP_7me2_*QvB|_'
        'tvC+SiB*xdKNiF-CV!Vja79)LuXmeqi?R;h50X)KpEX$?^`rE&Uk}Eq<&<!{Z4AFuSRP@u`&W+=+B|hZVOVgvqjtL$2Pz*l6<ZLX'
        'cR!8xCp`<g0JCeemTX{vDZuXB>+0I+@qq=l0JodBZIurkS|e;<$|nom4?H&xw!wA*J32mB)!NxN4hCR{fL%SfWF_0~7v{iD*d<_3'
        'm+#<9V_`S!5wLev9rBQU=#}ze5cUe#*NHXBzeDBjf8|^lf_(xGJeLD`$#-x~Sg;=s2spIZXX5hCn)Bfx91?K2FDHs1|B=_ig?Hev'
        'fOmWPMP9;t@3ryZ2)rxc=nMH$6vZ5SqZ;rY92MYo&)4xc#)4z?T*HYDj`t$ws_y&iQV)*92>~Y;Yp&P<)t^)ARs-ILlLAh^bWbS5'
        'qiBl#U|nm&DL5^lxVTPw64V(xv+gzE11JhO`^xL242u77LwLX$I4j`X^4^{#%;L)ZJ-=af;X^nlptPnwP!{D}*icSz9!df(c53WV'
        '&)cO9uLl?4qJYb5?geF1-jz+^2bbWofUB#|$~nTmxOiT!Z5kK20#^lm^jbZmY|6d9sa)Y2d?et;^82OO?i;;hZf-gcxDGc2+<NWa'
        '5d!6Z{8o6wO}HiClm6%MD%H55&f=$UjURjrp9uKujrvO{gz@=XT?2dyp9v^;do5Zd7uk3-NZOLQW1Yl;hLai=bez<&VBn;I1rsMt'
        '9I<fT!Vw$iZ5(lk#58&uPHX7tIIW{+;Ix6BiPI()DAd783kx<*+E}1#2g)#uWesOFEbBO{W7)u21Is4Pn&?rei_;c*Hcs2<IXLaW'
        '2+ZS%hVvSZ=s2(Ah=KD4j+i)aV%fr33(Gdn+E{jQ))B1=BenG%NzVJ|y5WO=jT&;*@8AtqL++LuYX1T(Y^k9QQA6%Jt0C`Y@7WDd'
        'LtgI={AbmW*ZIG||4I$1HJ@zn?v@%_R6{Oh6}QyTDmB!5R<_j8TGdeJ{Zb^~o-H->25PADeYB;9HbV_jk3}ndMweK0aE3^rtKpOe'
        'Q|RhArK4-$l!2~^Qzp)tIBemZg$o)E+ZgINXXAp7!w!Z9&N;+j28$ZbXjs&7M#rLoGX@q-oG~#palwRPn8RTW=LmqZDV6dJ95&G<'
        'R4QemYvYuSu7gt!E>ID|CYOaFm2ybnKnM#MQUwcVEG*hMW0M3@GosMqR%ZsqO~2NtN?wqyO2CI!%t8IiL}$YKNQQregBc(2Ypj_v'
        'H3F;2Cw!OxQ#8(MezTG0epHip`JkUQT4|M$BW8Xx$V15;^$|xE$+z8WWYPFNWqm4(T)RNE!-ksR>dlA(tBoX28?odr8_!vq1hE>V'
        'wkmN{^;0(5idEg^DQhOV-I@Fn^omKS)t$2LU7G)vE|o5p)D%$WYMeRbhe1Z{QZ--ASUMI}nS2ud8U7WP!b_cT+SQ(s-0piptrjJt'
        't449;y}@0=YP%)4tzLB*KD*oLcj<3@%${lU9smF'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
