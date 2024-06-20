# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/uavcan/time/SynchronizedTimestamp.1.0.dsdl
#
# Generated at:  2024-06-20 11:16:15.449904 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.SynchronizedTimestamp
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
class SynchronizedTimestamp_1_0:
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
    UNKNOWN: int = 0

    def __init__(self,
                 microsecond: None | int | _np_.uint64 = None) -> None:
        """
        uavcan.time.SynchronizedTimestamp.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param microsecond: truncated uint56 microsecond
        """
        self._microsecond: int

        self.microsecond = microsecond if microsecond is not None else 0  # type: ignore

    @property
    def microsecond(self) -> int:
        """
        truncated uint56 microsecond
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._microsecond

    @microsecond.setter
    def microsecond(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 72057594037927935:
            self._microsecond = x
        else:
            raise ValueError(f'microsecond: value {x} is not in [0, 72057594037927935]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.microsecond, 56)
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
            'Bad serialization of uavcan.time.SynchronizedTimestamp.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> SynchronizedTimestamp_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "microsecond"
        _f0_ = _des_.fetch_aligned_unsigned(56)
        self = SynchronizedTimestamp_1_0(
            microsecond=_f0_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
            'Bad deserialization of uavcan.time.SynchronizedTimestamp.1.0'
        assert isinstance(self, SynchronizedTimestamp_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'microsecond=%s' % self.microsecond,
        ])
        return f'uavcan.time.SynchronizedTimestamp.1.0({_o_0_})'

    _EXTENT_BYTES_ = 7

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e-CtK0{?YYZI2X15MB`Ojzux#2#K#WAH*ZFBN7iUe#0{)W@Wj+fiH<pdS+_3JIr*C-93A^Bqs7f5|T+Yq5W0<6MuzI&F<~q'
        'q1=bPnW^fkr>dTM`nNNG-Q4JPf9;ieR`{Y!Qcq6HQa_bhNlBX9s<vJSitSqugKP58ING1p6ko>c&*HCft38_<S;2m_k<(n7B<PBg'
        'hclBaXN`VJ#XdgxAgemI8|jps*VaVUYu6tyo?ph{sbTMVd=}gDsSLsCtO?}fPl)~+TuZOmp1rH7ELM2>X(5A51A~0s@!IK12R((y'
        '<|E_v#8B~#2{a*hvbghUrbAkinFJMwI|!ajAJWPe6xF5n^4?J(K9=mlc8^V5(eLp=Y%is#+!WFk#{<1+GIh2+U+LUgPq{TkY|o^H'
        '&Exm~obL7Z6$#T+898Cc;+U5gLCGMLoRX-e_f!b4O-{nwiiC7X;iQ|13a=&zZQ$Q|hNRCy7vB-oIz54TODB}v=)8DrB9or33++Wg'
        'V~w7On%qFvb*Xb1Fsejwn7nb0<1CMGrp8kr;};nTN53?fIF65<tya<fk`!GqQ2`ja8^RNHPPs)~U!zcMCiv>68nty$beFx4DgbUO'
        '%Z3<bu)@%k+k~HSX%FW3miF!21GGdO=mIz?m%#XCzc0i<-1>R@_Q}q|U1qik;?}L5Z80P1{0(uSbgtM`V{&1Zh&$r;=UvQWXMwu`'
        'cbqt|O<5ojG6>NaLpgaboi1l{2q1#c!7tIGZ8!$BJdtf=4azp2y}I-;7Y#xPiEIc=hZ_Ad0X!DD(_Z^zUd(O@F6ex)duJrJj1A)M'
        '*VhG@V9-m4e7STWMN@OXz7W|AyTuu6IV-K~W{g2$hm#KY{?VvJ#qcL^_DYr|PnhX8DQVET&r^(P)u@W_Vb0O8oC8SlabQ|-4;)(!'
        '1|!f!pF}Leg?3}t8eWsI+&i_YE-#+m8Sbce)%(L9?~}SRU!C<wqv7cOccZATw%2|nXJ1X-@eOn1Zagvez$CF<OFKZZ{oqIx=&%Oi'
        'Sc6VT!p4J+pRzo{qXz9cl$`Td5BuH4Gw*qCc<MQj`K-yP-8?2=X*QcHBUd5RMfHjLsDYpqgrry}D&mXwLORxmRHQtpR2Om7UQE4h'
        'Tuv~Ql-3e*(XR8qQfIL}w+A&o+~cn=Ay211g>Wd#@_V}0a0DNNvn4RnA-KggwC~kTh6PR?O`4MPt^^Xrtj%Q`akyu({qTRKJNYcR'
        'nQ+r$U|HKtmGl6|GLSA7HNL<w{vOR2pEC%~z^s7|SO-<$W;1`W+!Bi$4y=1J=r+S2%h}DYOA5vWbz;*Hz?RKi3py!S<-v>66NOzv'
        'cWnisD;9~Fx0yvGsML`fce^-+k97lIQ?AGQ7~gSGJfVa&IV;hkYe#%pNjQoQufE6j&98L$wtIg_OER}_q!w47cwG=bt1^rEpsV+&'
        'vI}v%kFAu!y46**mgWjF5Y>MB_MR+QBmd*1eqigUDN9@fuUggMkGM75`O{~(hwFKSINWG5)LCi6*Bc(>AwR716$iF3{yy&swu=cr'
        'YBFYe@-M0BlF>T|000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
