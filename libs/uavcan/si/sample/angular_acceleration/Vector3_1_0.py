# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/si/sample/angular_acceleration/Vector3.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:14.594797 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angular_acceleration.Vector3
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
                 timestamp:                    None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 radian_per_second_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.angular_acceleration.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                    uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian_per_second_per_second: saturated float32[3] radian_per_second_per_second
        """
        self._timestamp:                    uavcan.time.SynchronizedTimestamp_1_0
        self._radian_per_second_per_second: _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if radian_per_second_per_second is None:
            self.radian_per_second_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(radian_per_second_per_second, _np_.ndarray) and radian_per_second_per_second.dtype == _np_.float32 and radian_per_second_per_second.ndim == 1 and radian_per_second_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._radian_per_second_per_second = radian_per_second_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                radian_per_second_per_second = _np_.array(radian_per_second_per_second, _np_.float32).flatten()
                if not radian_per_second_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'radian_per_second_per_second: invalid array length: not {radian_per_second_per_second.size} == 3')
                self._radian_per_second_per_second = radian_per_second_per_second
            assert isinstance(self._radian_per_second_per_second, _np_.ndarray)
            assert self._radian_per_second_per_second.dtype == _np_.float32  # type: ignore
            assert self._radian_per_second_per_second.ndim == 1
            assert len(self._radian_per_second_per_second) == 3

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
    def radian_per_second_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] radian_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second_per_second

    @radian_per_second_per_second.setter
    def radian_per_second_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._radian_per_second_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'radian_per_second_per_second: invalid array length: not {x.size} == 3')
            self._radian_per_second_per_second = x
        assert isinstance(self._radian_per_second_per_second, _np_.ndarray)
        assert self._radian_per_second_per_second.dtype == _np_.float32  # type: ignore
        assert self._radian_per_second_per_second.ndim == 1
        assert len(self._radian_per_second_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.radian_per_second_per_second) == 3, 'self.radian_per_second_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.radian_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.angular_acceleration.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian_per_second_per_second"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            radian_per_second_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.angular_acceleration.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian_per_second_per_second=%s' % _np_.array2string(self.radian_per_second_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.angular_acceleration.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eh+kJ0{?Ya-ESSm6~A`k?>LF$B!nb{3DCrDa~E)MaA|1?Ms8rpCCUel`oVT~cYJ5$-JR{stnG`0R33`rYNf7}MarMRpTM7h'
        'L{)g?xlgDMea>5Y&feL3uY+SL`JJ7QbIzPO=Xd7*?eLe6=Ueq(@nY7COcZ;*;aaj-e#(NFdw!^rOc`l;Rm|V9IuC8G`Q2W|tB2L{'
        '=hbJ`QZeDDEP?rU&bC9AdPaJNB^m5yX*Z9V_E{M6m}_RGO1+PHXqCQN71RDU*9L|v(JH1scJjlDj?vZ^)#p_)=QC@y406j&^=Gj3'
        '3?B!ps$yb8@;Dm$HtR>sGT)-ZV!S^nCW?#BRVx$j-RY&F&?=Rm^5`xM7z^H4VoJ<3o`@r0T^x7Y7oX)vrez|n+y*}u@1;g|Qy#sa'
        'THfV)f5hheKw3ZMY1fL1u7Q^!GuBU31YVvmPTy)2;Wlp_=5FE?hUV|p?W#EGgO6#%bTq1HFAv~obBPSKGCWjiR27H)NQKq?|Bkm>'
        'cLgVDo&;PIwMj-+8Da&qM6hj6GG+{qh>>Z?iBSnBOoIu{bdMzPnOY)KSYNNS-YhD0<DgV&*@fvP>2dE$y$S<N0%rI!k%mNkQ$kEg'
        '#&w%zSuDeTN)S{N=31kk!4|ZX8$JscMFLJV|7#9+1KT&XN`~6a;QDH1Bmu{`zCsM=^`cOLUX#H=W!i;Ny)EHvwJWl=J`1M+=eAj#'
        'bM(?GlJac~6a2RstDU}ogZb5KZ3qe3krDXGLk2#+H9Jd4o2-1YdToDXVL1y_Zpq5Z+A8UBrp*<yBV;IW3Th;^J&#-`*WRdgj_d`$'
        'bI2V{c2pimU<fP_lBX#TxiL)3xYu_95`jo-2Hry0U>kUgH?j&=tx&naRkeATj&e{z7+3?vd{;ueQVV%ZLM@FnUjH!bG30^_+w0dm'
        'WGPjaY`nKjAQMuEr3QN;(~uN-hVgon1U)EHw3xA8tXO@=a8W=EUhVkZ=Bh}7?ss9a5iE}JhB4i`F>lw)`zAK|Fi;7HfqstK!974y'
        'T(+1N7z2&7DO?PJAR4cNLO5DXud5Wx#186CEQ$+Gx=7c=OX3yU!g>;y`=v8=uR}W@{k~I)<>JyGxK>Y_uJaA<4WqG@s-4uUib=nA'
        's48A)NP+KWkZ?$5`zT@hcAcLrZu}9e#S9!d#8CtD8&1YLZ_%+Yz%vu%0WTIuc+d}eeY(X{EQzz?s%YmxC=myvP)<Cm_KKtarrhO`'
        'j~C_3sOl68zEQajIZVXd&lu1}F@+Gzpekl=0mbj$!qJC7Ph+nFaR`N+KAuTf2>EEWior*|3%P}7D9&Yh00r!8jvNnmhfE8Hnd}oR'
        '=)ss(#f1Y&)_dK1&BLHo7HMtK7tDZjNCUnr)M^hd<J(TZ@X-Q63z#*)14;ucV6ZWNp|}|ouH8|3t6f)y8L?U4U2POH#)^HF1`1T1'
        '_qm{^f}tJw5V9+v)*!kn0iuhXVa(e=fhJ(7hK=i5+=ewuw@t=FxhY5T9U8?J_mGo=7(#TZ$(JF8!=dfd-&JwsU1>k8zwhutG8cz@'
        'l~o0KmJ-uT0tNR2QN76%<;d})47;$>!&WruhXQDz5`QX=-C_}P<WCj}hO?bKhF;!#dRDCdvs$8Sr3s*+XMGJ7oz4R|XChN<Zy>N;'
        '6sEAnLAIb$I)?jNB^`Ho2ywimhu!xC;#f&1-T0InpLRIo#%B>HOFHM)A3>Zh={(}$k{)&Ik0H*L^thW}K%6M)38!Zf@kB{aA|5a4'
        'Da4~CJ&kyzq|YJFmh_C<|Gcw%*4a7d^qhD0UO+ro(hG=ZOZp<>^CcySXG(ez@wt+|gm}87FC(5R=_`mQOZqd!#gblfeqBafDCv^('
        'ZyE7eNq_GA`~~8CNv}A6+wQ!c^ZQlAnUcQd{C^#Bs-!FK99LaD-f-us@AXhgueo!*>EgTQ&iBjyz0<cG{>tI69lq`GHx7U6@EwOY'
        '9Nu>*9PT=N;P8>duN;2u@EeCeIQ-G!<38S;9&^H(Mp$ZuwMMwn2=^O7G{SBpJZOYRjqp_?eBB7&G{O&!@M9x9c0vxXJm?J2Pmto>'
        'Sbzi%ooB`l-<``v3me$*wR!FtuU@TL58i?sNcDYwxQ;{npPKVNyu9&!=H9^Pi<u4R&vxG`Xom#a;flEY0K80C7hXm=zD3{u$3koL'
        '@5z%Vt}{V>&%moSW1+OYiXIa8#Qi=W{84-|LK`P;^Nd@0F!_x8Tey{p?g*8TvJOg2{~{9jmwr|?RAI!wI)jj%*DR7O^+BoM=kXB{'
        'qA0$D)+ydWKmIKi#Q((ixp;R^tarqF;&)5phIn6mAgK6I+!UQ++(4U~?Eh+kkRJ5Ar7DiQUoQK*mbkNr#tuGzIFLqTatdB1*s9Y5'
        'IT_=Mlnh-EfAk!v%@<pAtPau|1ZfR}RL4gAhZ`Jy1f!3Jqg%+wKN-eAdjAJHiC+c-4gdf'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
