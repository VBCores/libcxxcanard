# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/physics/kinematics/translation/Velocity3Var.0.2.dsdl
#
# Generated at:  2024-06-20 11:16:16.662382 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.translation.Velocity3Var
# Version:       0.2
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.velocity

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Velocity3Var_0_2:
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
                 value:          None | uavcan.si.unit.velocity.Vector3_1_0 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.translation.Velocity3Var.0.2
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          uavcan.si.unit.velocity.Vector3.1.0 value
        :param covariance_urt: saturated float16[6] covariance_urt
        """
        self._value:          uavcan.si.unit.velocity.Vector3_1_0
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = uavcan.si.unit.velocity.Vector3_1_0()
        elif isinstance(value, uavcan.si.unit.velocity.Vector3_1_0):
            self.value = value
        else:
            raise ValueError(f'value: expected uavcan.si.unit.velocity.Vector3_1_0 '
                             f'got {type(value).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(6, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 6')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 6

    @property
    def value(self) -> uavcan.si.unit.velocity.Vector3_1_0:
        """
        uavcan.si.unit.velocity.Vector3.1.0 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: uavcan.si.unit.velocity.Vector3_1_0) -> None:
        if isinstance(x, uavcan.si.unit.velocity.Vector3_1_0):
            self._value = x
        else:
            raise ValueError(f'value: expected uavcan.si.unit.velocity.Vector3_1_0 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[6] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 6')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 6

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 6, 'self.covariance_urt: saturated float16[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 192 <= (_ser_.current_bit_length - _base_offset_) <= 192, \
            'Bad serialization of reg.udral.physics.kinematics.translation.Velocity3Var.0.2'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> Velocity3Var_0_2:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.velocity.Vector3_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f1_) == 6, 'saturated float16[6]'
        self = Velocity3Var_0_2(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 192 <= (_des_.consumed_bit_length - _base_offset_) <= 192, \
            'Bad deserialization of reg.udral.physics.kinematics.translation.Velocity3Var.0.2'
        assert isinstance(self, Velocity3Var_0_2)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.translation.Velocity3Var.0.2({_o_0_})'

    _EXTENT_BYTES_ = 24

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`t-TW=IM6yDAK3JD>U0)^qe0W#s*QlQW@QiNm@B4`m(MF;PUi5+HVrZb*&w-Qo$C<@h7wS+726L>+rsIBOox1vgw'
        '`p9D+`3bzG=j?it4NZPQSta{@V;>(M+vD$?{iN;7&-)AYPqrhfd5P!SPQqeAeep3Z`^<LSuo8udkW6R&mt~x~GL6~0wTS6^dgQjg'
        'rAt}66VM9upNQG4oq93#?TFVB;U@M?5wHrCNM%fe#0MS*_7&!bu8_53S7@xWE@z&_3AAfo$U3hWeovDEX}P0s>#WzIQpTd3N|xwr'
        'Fyk7rE?McUeNr&rTaK~E@u;MZ#K3t=qmj2~J5oCD(!frHod!bM^CmEe(3N3)O!H3OO^T#|aqzxtnh%(<L)q3ff{0^U)7i#JQDxo*'
        '7R*XMj!i4~tlwcitFS;eLRxD@Q7kG#ig~c;p7cX1S9<An%0fDReG*M9Sfxu7=~O}wR=F$NG?Nd<VfF;{O<@;q?Wg(@1nDG_1|E&Q'
        'W=9L)r$T38KT;1Tz7bOwk1c_tnlv1Id^T8U{wyvo7D(|9xJ}DhHv|$<+(}JZvo@#f!{B}S8kgsS<;oYIb=LQekd2+Y43B2DS*sI9'
        'I<wYtlGG~Y&=;=GhNf60gdM~<FGeh;aFWY=*5SBZz^lQ}WE(EAh)J=!U5j%QV&~&vw|+YHeHzzZGy-4q)K8iILYIi8k}|Bk&8dh$'
        'lj}%m6-g(aN9t4bN{VP&P^86RtHCyd?TAH1I?Qt?V!I+;=D8cOLy;bXy@*|k^qKyCW4{iuPm%S;Zou>pBK9h>!L$#V`8FaBC^Bru'
        'Z8CmeL2OfGvl;&?;;<rH5H~2Y6>+^H+swGv5W5xGZv5{+Y*oZE<98x%S7aCBHbr(LZc$_p;$}tmB5qP-AL2$u_M3T1CcY8Gb&4D?'
        '^BqL&QRI+`cht;lo4CgiTNF8L=0AcsrpQr5Tajakqlz3yJfz48#Dj{wj(9+kHxNe@If+<O<W0o=ikw2+r^so<y^5Sc+@r`_h`SXz'
        'i?~aXbBH??dAsq7kn?7pS53Se@wy^ag9`@l8+>5!k-;YhpBj8-@OcBLx{8Ku&PgdJCv$Q>Cs%XAb5hO8LQd}I<Uvjz<>X0Dp629P'
        'PM#Z*f|Rgo1j>(^VcN=gQ9yhLDonE2flCE9*bM_u!=>>;xWNU`5Sk4&$-YyrHL}bt&A;MX5|BQRMKN=!WS+j8t#fXm-a1hjOGkKm'
        'IvaG7FpXUX9X@j+3c{9kBKV>VqBa9btvZ9P_u#S@$6#(AVis$O1Q<d%G7f!EJXVDu0}6C&l$JqY97uC;onhYPoC50B(MToWAOQz$'
        'm`-4Ho=|i)U{Z>G#6E1JglUNqJmheiKzK3c0ucXs;WB-ff6c$)C-}*_%<$9vtjRicHJYKGCxY4kNEY;-gJc>tx;5#7U7jM>`851r'
        'd?`LJ#pnMfKK$Veiqqam*Lb_&d8w4++YQ^v_ZYUH4Db>^#77sn&5um|vzV7Q{5a`Y{bo)WHVFpf{CvZJG+v$h{7rW;zlsTeIK33z'
        'IyaoBQ2hlUT4^jH%xwJqQe7m+8Ui`;!O?5hdl6jx(OArKX-PDn^_dmkuq0>JvIh&w?pRc92$}J3A+EWxVxhnX=OzH=4#QW<zq`x7'
        'pXNXCA4~iv{xkoD|H^;kzh|u=a8N<lD|yt+MlG+ip5<yDYVxLfUT4G26+P(N(Pf3>e}I~0A6|g5G`4a*v_2A&H-&5WTr8vdF<1tL'
        'b#akc@JFr0{N|v(m850VT3qW|W&359LZMcdSiSlw{k6oJHFbC*3^0`hs}_w|&SK378jU|cR`vEL|C<z79&-I`=T5;^vjjUHL&xK#'
        '4zO<s^vY&@7wmrl(|L~6m<<2`'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
