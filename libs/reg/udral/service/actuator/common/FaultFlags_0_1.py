# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/control/external/public_regulated_data_types/reg/udral/service/actuator/common/FaultFlags.0.1.dsdl
#
# Generated at:  2024-06-20 11:16:16.225729 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.FaultFlags
# Version:       0.1
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
class FaultFlags_0_1:
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
                 overload:               None | bool = None,
                 voltage:                None | bool = None,
                 motor_temperature:      None | bool = None,
                 controller_temperature: None | bool = None,
                 velocity:               None | bool = None,
                 mechanical:             None | bool = None,
                 vibration:              None | bool = None,
                 configuration:          None | bool = None,
                 control_mode:           None | bool = None,
                 other:                  None | bool = None) -> None:
        """
        reg.udral.service.actuator.common.FaultFlags.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param overload:               saturated bool overload
        :param voltage:                saturated bool voltage
        :param motor_temperature:      saturated bool motor_temperature
        :param controller_temperature: saturated bool controller_temperature
        :param velocity:               saturated bool velocity
        :param mechanical:             saturated bool mechanical
        :param vibration:              saturated bool vibration
        :param configuration:          saturated bool configuration
        :param control_mode:           saturated bool control_mode
        :param other:                  saturated bool other
        """
        self._overload:               bool
        self._voltage:                bool
        self._motor_temperature:      bool
        self._controller_temperature: bool
        self._velocity:               bool
        self._mechanical:             bool
        self._vibration:              bool
        self._configuration:          bool
        self._control_mode:           bool
        self._other:                  bool

        self.overload = overload if overload is not None else False

        self.voltage = voltage if voltage is not None else False

        self.motor_temperature = motor_temperature if motor_temperature is not None else False

        self.controller_temperature = controller_temperature if controller_temperature is not None else False

        self.velocity = velocity if velocity is not None else False

        self.mechanical = mechanical if mechanical is not None else False

        self.vibration = vibration if vibration is not None else False

        self.configuration = configuration if configuration is not None else False

        self.control_mode = control_mode if control_mode is not None else False

        self.other = other if other is not None else False

    @property
    def overload(self) -> bool:
        """
        saturated bool overload
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._overload

    @overload.setter
    def overload(self, x: bool) -> None:
        self._overload = bool(x)  # Cast to bool implements saturation

    @property
    def voltage(self) -> bool:
        """
        saturated bool voltage
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._voltage

    @voltage.setter
    def voltage(self, x: bool) -> None:
        self._voltage = bool(x)  # Cast to bool implements saturation

    @property
    def motor_temperature(self) -> bool:
        """
        saturated bool motor_temperature
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._motor_temperature

    @motor_temperature.setter
    def motor_temperature(self, x: bool) -> None:
        self._motor_temperature = bool(x)  # Cast to bool implements saturation

    @property
    def controller_temperature(self) -> bool:
        """
        saturated bool controller_temperature
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._controller_temperature

    @controller_temperature.setter
    def controller_temperature(self, x: bool) -> None:
        self._controller_temperature = bool(x)  # Cast to bool implements saturation

    @property
    def velocity(self) -> bool:
        """
        saturated bool velocity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity

    @velocity.setter
    def velocity(self, x: bool) -> None:
        self._velocity = bool(x)  # Cast to bool implements saturation

    @property
    def mechanical(self) -> bool:
        """
        saturated bool mechanical
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._mechanical

    @mechanical.setter
    def mechanical(self, x: bool) -> None:
        self._mechanical = bool(x)  # Cast to bool implements saturation

    @property
    def vibration(self) -> bool:
        """
        saturated bool vibration
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._vibration

    @vibration.setter
    def vibration(self, x: bool) -> None:
        self._vibration = bool(x)  # Cast to bool implements saturation

    @property
    def configuration(self) -> bool:
        """
        saturated bool configuration
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._configuration

    @configuration.setter
    def configuration(self, x: bool) -> None:
        self._configuration = bool(x)  # Cast to bool implements saturation

    @property
    def control_mode(self) -> bool:
        """
        saturated bool control_mode
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._control_mode

    @control_mode.setter
    def control_mode(self, x: bool) -> None:
        self._control_mode = bool(x)  # Cast to bool implements saturation

    @property
    def other(self) -> bool:
        """
        saturated bool other
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._other

    @other.setter
    def other(self, x: bool) -> None:
        self._other = bool(x)  # Cast to bool implements saturation

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_unaligned_bit(self.overload)
        _ser_.add_unaligned_bit(self.voltage)
        _ser_.add_unaligned_bit(self.motor_temperature)
        _ser_.add_unaligned_bit(self.controller_temperature)
        _ser_.add_unaligned_bit(self.velocity)
        _ser_.add_unaligned_bit(self.mechanical)
        _ser_.add_unaligned_bit(self.vibration)
        _ser_.add_unaligned_bit(self.configuration)
        _ser_.add_unaligned_bit(self.control_mode)
        _ser_.skip_bits(6)
        _ser_.add_unaligned_bit(self.other)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of reg.udral.service.actuator.common.FaultFlags.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> FaultFlags_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "overload"
        _f0_ = _des_.fetch_unaligned_bit()
        # Temporary _f1_ holds the value of "voltage"
        _f1_ = _des_.fetch_unaligned_bit()
        # Temporary _f2_ holds the value of "motor_temperature"
        _f2_ = _des_.fetch_unaligned_bit()
        # Temporary _f3_ holds the value of "controller_temperature"
        _f3_ = _des_.fetch_unaligned_bit()
        # Temporary _f4_ holds the value of "velocity"
        _f4_ = _des_.fetch_unaligned_bit()
        # Temporary _f5_ holds the value of "mechanical"
        _f5_ = _des_.fetch_unaligned_bit()
        # Temporary _f6_ holds the value of "vibration"
        _f6_ = _des_.fetch_unaligned_bit()
        # Temporary _f7_ holds the value of "configuration"
        _f7_ = _des_.fetch_unaligned_bit()
        # Temporary _f8_ holds the value of "control_mode"
        _f8_ = _des_.fetch_unaligned_bit()
        # Temporary _f9_ holds the value of ""
        _des_.skip_bits(6)
        # Temporary _f10_ holds the value of "other"
        _f10_ = _des_.fetch_unaligned_bit()
        self = FaultFlags_0_1(
            overload=_f0_,
            voltage=_f1_,
            motor_temperature=_f2_,
            controller_temperature=_f3_,
            velocity=_f4_,
            mechanical=_f5_,
            vibration=_f6_,
            configuration=_f7_,
            control_mode=_f8_,
            other=_f10_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of reg.udral.service.actuator.common.FaultFlags.0.1'
        assert isinstance(self, FaultFlags_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'overload=%s' % self.overload,
            'voltage=%s' % self.voltage,
            'motor_temperature=%s' % self.motor_temperature,
            'controller_temperature=%s' % self.controller_temperature,
            'velocity=%s' % self.velocity,
            'mechanical=%s' % self.mechanical,
            'vibration=%s' % self.vibration,
            'configuration=%s' % self.configuration,
            'control_mode=%s' % self.control_mode,
            'other=%s' % self.other,
        ])
        return f'reg.udral.service.actuator.common.FaultFlags.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8fDd$L0{`t+{c9XW7*3kxa!Ef!YQPG1f>IM`_mrxj6*MhY<eD^^TKqv-XLsjr2IqFxnb~Vj5Da3mF!({oKT;4s@E`D*`_A1J'
        'QU!l95N`LK_j%s$clPVWpWit<*Zp&si%w=T8O4TaL8bVTCXz*Qs#=9I!ZPp99#~zbw$$uir(piE-#+qR`7O5;=d^|MtC}^VGSgH>'
        ';Ao4KMHK4PDjk8QrSj-DEv3CJY14RDjoVBcp>ogX-17bY^J8D1tIt35N8X)|skK@prDeu{3PVqDaj50p(rv+HHgat>&Zwoa4gNj}'
        'UTD!0R<xmU`leEn(foLPr{hG}ShBonxv$TIG^NJIEtN6PFS?EW0YQL8w{W%_jzT2g`VYOk7#mCTjOuKh=uw&QC0A8Qf>bo~ZZXbO'
        '>fNjNI3qzqgdsG+IXSqyLzE^+FUy&x7I`8Glj;Gnyn7mXkX`7x%h&lv|LNKKJio-B=a+l7mfK2N+Jw`aZu_7t3fUoj(a09;`~&K>'
        'mO_<d%UVTn5G@jn%$*3kk*eHkB_*38xN>jw{%>8Zwt-27?F8cMA;~l`N}_GZ;Do3~m-Be`pUTQ=i=~|ABBe6ed3{*Sl;*jzaGYcs'
        't&)?h1hpcRj1Z(jg+!<)GqutdNv|1#rCP8wMm0Pnk|93A4pYW5^K{XiMQIwMS&q!Scxzk|lGGB$h`br9BJwuIDmxkXnSR;(bF}H+'
        '3K3}bMahh1NLcTfgyUc*WY3^!l@6y#ryI#|zXX%#+?jovWpL*B7U1jd((KW1D}lkQ-p9}Q$ivl&fsZ`mn>;#6FiQ&F=x&1cRL%yC'
        ')N7zElsi-UnkiT+8Y0~e-ZHm7w%+2T(_5l}oA5RM5`TeT<J<f?ukkndYy53~gTKpnc%8q;Kj6FkGyX}5#gwr^vy>tu{*gNuH^d>!'
        ';*g>kf$h1q*r-yc3<r|M1;yHN%i%|g#JiP!EcV0wAbpHAH($dJ;wo(NQ-y$HzXC`QJG4yaXleIcQ6^HPF?LZYgWb`B#Y$g*7)!W&'
        '2Y{e|3xHryC+{k~o4~vE(OnR|9K8~S`gj}m<$BDifw!9FHXd+1;+r3TG(R`DgT}zBNW1NaG-u3WXwVUjKt~#Z4~>{%2yAG}LMxQI'
        'Wr8A5qt@vY2ZgrCn2uI=#yCR98D_}?j!_NjsnVL6LgiVPm1<NANg2+SumI2oO5a^rK?wm+vV~#WCN$V@h<s$e*Aq8Z4P%5`TbMU%'
        'HI_#Y#OI=5nV^x<&02V?9e_0+vc`cGz8b8RU;|sqV#IOjkkEKzzF$2SCTCPyP7GJ2%t(I~?cLpde{bhb6fU1cqJUQhb27T9Pysvn'
        '?%kQ2!rtk=AK<k=H*NubdPkl_Vmhrvp?gr`UDi^V!cfJ#-O$h*!wa_(r(9rw`H?%{pXezi{*Zq&d^&Q^U@wI^$Y)Zzl^!EHDtt(c'
        'A-|i!_I+;&{Pe%(f1`;i@0C(g-I=OeCB}_XGXI0$s?Yyu5_~iky@tStSec-0TOtqNWO$&5;bA%4Cs<7Zy&AK_g67@t%02AqUwV%G'
        'I$&d1^1s(l@jvkYCl3A!O1}l-Y4L3A0+be}u@mCi*hMHUPGcv;v$0E1TAIdAh-YIfP^wI0C&aU{%TQXL#!iT5W2;cAPGcv;v#~2s'
        'TA9X9h{v&&A@)3!&QD_}#Ix;QfYOC=Y_*&go1{#lzXAF+E~HBh000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
