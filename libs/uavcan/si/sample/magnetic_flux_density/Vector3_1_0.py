# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/magnetic_flux_density/Vector3.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.477666 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.magnetic_flux_density.Vector3
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 tesla:     None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.magnetic_flux_density.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param tesla:     saturated float32[3] tesla
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._tesla:     _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if tesla is None:
            self.tesla = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(tesla, _np_.ndarray) and tesla.dtype == _np_.float32 and tesla.ndim == 1 and tesla.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._tesla = tesla
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                tesla = _np_.array(tesla, _np_.float32).flatten()
                if not tesla.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'tesla: invalid array length: not {tesla.size} == 3')
                self._tesla = tesla
            assert isinstance(self._tesla, _np_.ndarray)
            assert self._tesla.dtype == _np_.float32  # type: ignore
            assert self._tesla.ndim == 1
            assert len(self._tesla) == 3

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
    def tesla(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] tesla
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tesla

    @tesla.setter
    def tesla(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._tesla = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'tesla: invalid array length: not {x.size} == 3')
            self._tesla = x
        assert isinstance(self._tesla, _np_.ndarray)
        assert self._tesla.dtype == _np_.float32  # type: ignore
        assert self._tesla.ndim == 1
        assert len(self._tesla) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.tesla) == 3, 'self.tesla: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.tesla)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.magnetic_flux_density.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "tesla"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            tesla=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.magnetic_flux_density.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'tesla=%s' % _np_.array2string(self.tesla, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.magnetic_flux_density.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?YaOK%*<5nfW_Ta-jml4VJjT8<-;i8!_?Q)Zmlu}p)J)7Dzh!x8fEq-UnN-Qc{^-9zpgFc2SNh{gaOKpj9o!9T%2'
        '!9W5#N1v06kwebDDOIyQyGxlOAbqv{sH(26`l{!zhyVVc`Bwc`Ud(%uj$+T(TuBzok693N&kwUC&$Kk$mh*RwDne5zey^8v`^YYT'
        'YCo|{<%FNI1m?Yh?Sw4#wDdGfa@d`)PRfl8{jIp@`Vmh-QP2C3hbB|kY&q@kaHVCITG1+}K6LUUOUG#IGyAD6=X_?2l0jj(wtoUs'
        '&v0_E%9azGlE=}|xmiDAhWQ3P7UTUvF;QM}z8aZu?`|&*h00R-F^}%SfHvU16;ooS@kAT}>*BcEzW6LZawQXK<PP|;cpnZ6r;pxC'
        '4exNZKV)-$AdMgMv}1&&>)>U`wDFTH0x!>(r*AikaGSRQbGL8`L-RL#$Cf93@G*^;ibfUf6#*P=E|H<iG!L^hvgKhv%0m0#zvHde'
        'J;6y@Bmq|>+ae>YG%<o1BG?WmIn$a)M9VbfL}v*nOo0i-RF5R^Gc`n}u)bbtyjfK0#zASOWCx~~q{qFh^(qW737F=~L~0W8EeSCp'
        'Iaezz&tn-f19$EbR1+3Tp`O7Ov{Yz53l~KKP89!30e1u2w^Wu4wd=w4)yhZ$j&XIBXwK_JVFr424hNNK2S(M7gtOJI$lCfWoC2KN'
        'VR6CHOOuh5?_ikVzpXgi?fW;FU%S2nAtAdm0zY}kz{fXcX9-y$s~@dh-yd06&VsBkWOa3Yjr2HE`YPEKG88xkMUp~AkQ?OsYqidi'
        'z2J8NxueK#R>Tn)0t<u`Y05*cHB&O~^<98OAkyf8w-7ei2HxV0tbtV{vO?pk+B{501*jkltbt<Ql@PDgKpvA&NiDV4Kg>o9xgf)p'
        'jT>#UlxBu(zPn5y6H<t!0(&7-kQ7CZ@p_#EJt$JNn6qA-vHFhTqJSB^+VOkMRgnbU@4#X$SRCUGW4d)>zEUsmo7m#RKqVXo`Z;O_'
        '_W((8#b8=s3>40$a4`ges67jXaI~D>$Wkm5GpIYUC@whZ5?vQBikD~$>q%Vcm(JAvHf?|KyS5d}<>lXVl|5~`&NsL>jK+4F?WUeB'
        'C;i$XTfWec0`KOKa7bqRC}H|eou4dj{1I#A3>-PcQ4RB(PR2TK(Xr3KGaVEGFBeC6&<}cjzQt24iL>IGSSf%|A`V8OoOopS%A@|4'
        '?DELRi}Gb;+vS3<vqFU&CSvaA4CtbqLWpHx%bDB2@!i`v`UvQ0>}4Phks+y%=Mok|J{pz9;3MxsZs8fqb9oU!0sD$~iWuz<nHCN+'
        '*(X@ggE6z^g#$^}d)0fz!=PD%w6^FArolO+0pAs>-Gj^cN4sD6Xn~*w%o^Z<OaUukurYt3xEU0#+0E4UN?jRx#AbbWwNc0zBlcAq'
        'D9GZX&jmFV4DG-VAv*$U4WgSRKy;BajCmVmpb1#2VdJ_McVJDXR&>roxg|&P9U8?p_mGo=7(#Tp$(JF8!=cU7zioNs9ckXLf8XVU'
        'WG)Z+S#C@6EG4>^1R2~9MD-R=GDnUdKvgp6zQa~D>4ySnz=}VX$8NI-Ir2w~1jE^O5y#L5o}LwJU)UwOUg-cDdfwMy>2wjmITM*;'
        'djo-WQJBIO2iby3=@{;7Rdn3pA;j^D9(KPc5XUMy>Bgtr__V_rH$ICvS<yMS{s`i9MduL@SM;b`e++T1qQ~9*0^&qPPdGh`h$kv~'
        '67hINPaz(y=xM|w6@3nIwxVa;{^y<Dv(C;rr{}!0_X6U%ie5lGThWV%&sUTno~h_1#OEsdBI4<a{si$<MPEWZS<#;&E>`ri^Xm%Y'
        'LPeLHf6Iu+D*7|$=g$%6D|*%WyW-C4Ilo^<oT=z5&i_{trz*PY&T-Af<284l`d$xJ^twCO>n^_Q?tH)K-#dN7;V&Kj%Hf+1-*WhC'
        'hi^N)>F|L=;jruQp~J@xzjXMO!>=8F=kR-nKlJg|^q3RQG{RCNtT)2VMtIN&q7k}{@URgcH^P^V@Kqyx-3Z?`!uO5vgA)pP<w0kF'
        'eu5P5#sVaG=sYuK`0iXTTiC#cug!DMc=am9dhiz9M5^!e!wnqT|J0oKdCc*B=H9^P%b88+&t~5$Xom#a;i|au5WK`^yEFy9Mc@2<'
        'p*8yV<jE7)nV`OB;MJP55Z?5b9uoJ(gFYYpL3}hq8z=7Y9KHb#CZBPC8@Dpi8KDwV)j^5rpG5-y(obwd6<YkWJqXzZG(%t#u`IrY'
        '9x2{NgWre+@jvmeLcFslHrnD{@tY-aQ@kgBE2wy1+!F0_Tth#b?0=uw^3;J}D7HNAzESq~CvkTVtsQ*Qa3GDI{uI1HuqmepvM)vu'
        '$rt(^e%>6Y%@^BrtPaOIgkv4UQAa`in`<0>45N>Squa>5KN`l6dH)BM9=-(b4FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
