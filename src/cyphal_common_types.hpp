#pragma once

#include <uavcan/primitive/Empty_1_0.hpp>
#include <uavcan/primitive/String_1_0.hpp>
#include <uavcan/primitive/Unstructured_1_0.hpp>

#include <uavcan/primitive/scalar/Bit_1_0.hpp>
#include <uavcan/primitive/scalar/Integer8_1_0.hpp>
#include <uavcan/primitive/scalar/Integer16_1_0.hpp>
#include <uavcan/primitive/scalar/Integer32_1_0.hpp>
#include <uavcan/primitive/scalar/Integer64_1_0.hpp>
#include <uavcan/primitive/scalar/Natural8_1_0.hpp>
#include <uavcan/primitive/scalar/Natural16_1_0.hpp>
#include <uavcan/primitive/scalar/Natural32_1_0.hpp>
#include <uavcan/primitive/scalar/Natural64_1_0.hpp>
#include <uavcan/primitive/scalar/Real16_1_0.hpp>
#include <uavcan/primitive/scalar/Real32_1_0.hpp>
#include <uavcan/primitive/scalar/Real64_1_0.hpp>

#include <uavcan/primitive/array/Bit_1_0.hpp>
#include <uavcan/primitive/array/Integer8_1_0.hpp>
#include <uavcan/primitive/array/Integer16_1_0.hpp>
#include <uavcan/primitive/array/Integer32_1_0.hpp>
#include <uavcan/primitive/array/Integer64_1_0.hpp>
#include <uavcan/primitive/array/Natural8_1_0.hpp>
#include <uavcan/primitive/array/Natural16_1_0.hpp>
#include <uavcan/primitive/array/Natural32_1_0.hpp>
#include <uavcan/primitive/array/Natural64_1_0.hpp>
#include <uavcan/primitive/array/Real16_1_0.hpp>
#include <uavcan/primitive/array/Real32_1_0.hpp>
#include <uavcan/primitive/array/Real64_1_0.hpp>

#include <uavcan/si/sample/angle/Scalar_1_0.hpp>
#include <uavcan/si/sample/angular_velocity/Scalar_1_0.hpp>
#include <uavcan/si/unit/angle/Scalar_1_0.hpp>
#include <uavcan/si/unit/angular_velocity/Scalar_1_0.hpp>



using Empty = uavcan_primitive_Empty_1_0;
using CyphalString = uavcan_primitive_String_1_0;
using Bytes = uavcan_primitive_Unstructured_1_0;

#ifndef ARDUINO
using String = CyphalString;
#endif

using Bool = uavcan_primitive_scalar_Bit_1_0;
using UInt8 = uavcan_primitive_scalar_Natural8_1_0;
using UInt16 = uavcan_primitive_scalar_Natural16_1_0;
using UInt32 = uavcan_primitive_scalar_Natural32_1_0;
using UInt64 = uavcan_primitive_scalar_Natural64_1_0;
using Int8 = uavcan_primitive_scalar_Integer8_1_0;
using Int16 = uavcan_primitive_scalar_Integer16_1_0;
using Int32 = uavcan_primitive_scalar_Integer32_1_0;
using Int64 = uavcan_primitive_scalar_Integer64_1_0;
using Float16 = uavcan_primitive_scalar_Real16_1_0;
using Float32 = uavcan_primitive_scalar_Real32_1_0;
using Float64 = uavcan_primitive_scalar_Real64_1_0;

using BoolArray = uavcan_primitive_array_Bit_1_0;
using UInt8Array = uavcan_primitive_array_Natural8_1_0;
using UInt16Array = uavcan_primitive_array_Natural16_1_0;
using UInt32Array = uavcan_primitive_array_Natural32_1_0;
using UInt64Array = uavcan_primitive_array_Natural64_1_0;
using Int8Array = uavcan_primitive_array_Integer8_1_0;
using Int16Array = uavcan_primitive_array_Integer16_1_0;
using Int32Array = uavcan_primitive_array_Integer32_1_0;
using Int64Array = uavcan_primitive_array_Integer64_1_0;
using Float16Array = uavcan_primitive_array_Real16_1_0;
using Float32Array = uavcan_primitive_array_Real32_1_0;
using Float64Array = uavcan_primitive_array_Real64_1_0;

using AngleSampleScalar = uavcan_si_sample_angle_Scalar_1_0;
using AngularVelocitySampleScalar = uavcan_si_sample_angular_velocity_Scalar_1_0;
using AngleUnitScalar = uavcan_si_unit_angle_Scalar_1_0;
using AngularVelocityUnitScalar = uavcan_si_unit_angular_velocity_Scalar_1_0;
