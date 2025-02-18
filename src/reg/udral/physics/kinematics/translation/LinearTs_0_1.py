# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/translation/LinearTs.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.647346 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.translation.LinearTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.translation
import uavcan.time

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class LinearTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.translation.Linear_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.translation.LinearTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.translation.Linear.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.translation.Linear_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.translation.Linear_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.translation.Linear_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.translation.Linear_0_1 '
                             f'got {type(value).__name__}')

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
    def value(self) -> reg.udral.physics.kinematics.translation.Linear_0_1:
        """
        reg.udral.physics.kinematics.translation.Linear.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.translation.Linear_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.translation.Linear_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.translation.Linear_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of reg.udral.physics.kinematics.translation.LinearTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> LinearTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.translation.Linear_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = LinearTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of reg.udral.physics.kinematics.translation.LinearTs.0.1'
        assert isinstance(self, LinearTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.translation.LinearTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 19

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{^vGTW{UQ5k8W2J(4f7e7EDQ-PAs6Ejm^rTXEvni4522S|^4jw?;2!mgMT}O1zazN;&}wG!HH8fItbD1^m?K{Dl03'
        '04<U}`msQPBE6t5eF@M4?hLs+7ul+i2OBWIIlIf5*_qjIhx*mf?|y%<R{Tp}4cm@#T*Fj6lFXGKG0WwKX$M{yC>irS-Mbt|i5({q'
        'UulOtf1J;Joc}U!q{F7qJea=}@s^P|5p#`Dw3W1#u`Ye?u^7cTV!m=g4t(P_46|rO<>{EY!6OA@xu~V1KhpB!oYv^TZ}N}xbi!nD'
        '97!vQxypYI)^_l-vno%AZ%XbuUH|H)!(wK}=(HFt2gPuDCSe;k^Nm<~+*oe=wuk~>e#D&>7*H|u!d#4saXLV2=!uvF>*9cZeR?N9'
        '!bo~DmK)&5^gUn6md~B{{g}6S)E~78(~`02a=#UeoGyTuHdC?b1rB(5Dm`+iQiQJ=i!ir@QxKYgU*~u8^pFWY`VNbnUPX@*3$`}l'
        'NjnM@w*%kF(;?Fd?EL=U2Wzzz!HJ)E7LQ1<N_ti)5(^d+!8SMvnNr*#O8Pb@D)2aA5txWr)FvMM^kX7@SYND+jXEmT<DfK%WDBMn'
        '(%{C0Vig9MSWNL5A{BA?DrDawA&+KR7`oCfYl5H}JBcFH(|H9gC5qP}QN-dT;=f2BH}Lvu6nI_js*}D#8S%g|9$g@c^J0-5fL;~C'
        'My20^(P%@$-U?S_VZ9E!0OvNCn{f0p4v5b;Fih}Rb%V{)zs~&p<yi;`*_00W$!!KcUai*&nI&@%<}de07M3$BNMbTKw=hrIQ2FWt'
        '*%Z<iI2A(X;<iEFC70hUboRUpekV{n5!nn9*8xLdfsn-axy_Ygk#yUo3s49|#;W5jgbiK;Z!shDU^Ny&qHtAV9;TfHR1gN%Kr!Ev'
        '5HCN5Iwp1`l~hK#nMD_BLE5v6?>0%p4`Ooj#tbP=au`Hl&t?%6MG|7Xt`MsYhZHS_tnCJ@$T1`e$iXNaU#U_>JaoSWi<Mxmiy6jp'
        'Yq@;3SYDb~<=sGe90tl7jXQaOqBtL8Szrtzob@3w1cIoH91g<1bZjy3@tDM&b0?<7X)T?h3*xMJjn?oyiSy;r8NJt}%@2Ou%*9N4'
        '?k7A7wwo^M4f2N3SoecX-^kMuvv4R+U#UoeZ-r2BNM?PMFm|`7Pv%zsi1~CJwrt}l(&0@lcPQ{~uB^o3>2wbdnpV4{T--%NoDgq_'
        '*#rp1;b0Vw6L<1Q={|E+ZgI!NM48gbo9UFPf+VszOt{<(8PG*Kir`8sPsi^7&2Qbo(Z@hf0~difM1Z_L7)n?O^%zHi3qJBKs4d(>'
        'dNNEbIKU<lf8wIuF4MwhMoNMOJs7h*J^ezGH7*&i8yK`aMp~OT1ykT0(txQCYW@h4@rP!4@X-Q63s^P413?6=fWgN4g~QF@;KrLl'
        'v_4y$4Ao<^$X#I+Dkc_vCk+$?Zc=hVK?Pkq@I%O!fU^eC4Ll$^M;pevwF1xtELE{_aTYgVO%TnhklS)q_S8FE6zkkTPPSYK(YdN#'
        'x)ctZj<^5L)5-T_e7pF)%sa)L?lFTfPsvV7RNJ!x$PYwyiF<)2#}D9CvN(vkSJ8-R3!s5q{4CvnhdIcR&n*%RXPb%Z!ZomcR?Po4'
        'Z_tHIS#Y6;rG}i2B^K<{lRjQ=Ah0bIM)8V+YC)xR0N<-+bWr0S#KDXX>EFYM0~sCB<D+_fOyjs7uOp6RbV9G6L>$ZLUc{k{?$hh{'
        'BTi)WfS#X19M0%Lt!EnXU`7ui9?0ln#C;h(f;gGcqlop49@Fn1*LF{6J14cCQ`+7uh$l088u3I%Uqw8gQG$3Zqh}D0X7nuLk&J!|'
        '@o+|8Lp+qxZzE1;^qltVJmOSF8`{4a#Qholj`s7rh<h`7LHj$a_iJdsFCva-^mXn3CB)H;&gp%;q2uwU-cOO&JsG{M_jN_bcR}y('
        'tupWQs>Zi9zN7J)#_wtTzQ*esZ)v=*QE1%K_)y~$jh|}#OylPopKAO{<JToFjSXnwSS2(nVWARkRl@yB5S6f12@fmbNhN$*37=KM'
        '=aulZ627X0ueFdsmj^ck+$Tu!ddxzChnr_S?)IHCX$>#1PPf_9wqE>(U3S^T>UMft6WgQql<tO=G!p2EjFLx;Wt+K`j-E!iN5!dh'
        '{3cxXabI@}cPoLrbxxdr2wV183sff9*k1c&s@D7O*|TT*nk!;3>~XkTVE^LF#A4z)P|M%MpOtv;kyvbs8{!8IaZ9`}ekiE8EtW(x'
        '9aL~P4WY+y-{>AV-Cug$f3t|?N2pfZ6ZcEb`l)!(p*FiCwR#AR0HKL><T2sGemwZ^!`vU6ot%vo-$upfOX2bhLwkB#Xg9bU*b;ia'
        '-Glp==fWxex?2nn6frb`qD}n;&=bzJ`arF=HUy8IgDU<Z{+W(dUgqLoFE4yuBRhxh?6&YR+vYCbKUm{0Cxj=rhj6E8HZYoJcaP>|'
        'uhTCxqT37=u5xs>A^sztt{n$g#edhXpxY<lk?i1hx(8SWzN8DD!7j06nmny{xdy(?d)Nj}UCB3a<}PhJb?MP1_%JCx5SbfbkLD8w'
        'pBzTM+vXqiG#`hdm&fMTe_<Dsj+adg^o{sug8#2=jl$lGA8SpJc3S`M9b&yU1ut=h6W3wldS{}uzJGY_VrTt_F!AB@>-&dwE{DsH'
        'ioPU%A*R+WOyZw*O5NI9nB1%QcpD$@;Nu!R(y8jtE-y&Y?sfQ0gJ*U&w*Z@4=mz6PCm2s);>q*D=pV*l82<w)tjf}<5&!@'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
