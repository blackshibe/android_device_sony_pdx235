#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
    blob_fixup,
)

from extract_utils.module import lib_fixups_user_type

namespace_imports = [
    'hardware/qcom-caf/wlan',
    'hardware/qcom-caf/sm8350',
    'hardware/sony',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.data.cne.internal.api@1.0',
        'vendor.qti.hardware.data.cne.internal.constants@1.0',
        'vendor.qti.hardware.data.cne.internal.server@1.0',
        'vendor.qti.ims.rcsconfig@1.0',
        'vendor.qti.ims.rcsconfig@1.1',
        'vendor.qti.ims.callinfo@1.0',
        'vendor.qti.hardware.data.iwlan@1.0',
        'vendor.qti.hardware.data.qmi@1.0',
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.hardware.dpmservice@1.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.imsrtpservice@3.1',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'libmmosal'
    ): lib_fixup_vendor_suffix,
    (
        'libwpa_client',
	'libOmxCore',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib/libwfdservice.so': blob_fixup()
        .replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V3-cpp.so'),
    'system_ext/lib/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'vendor/lib64/vendor.semc.hardware.extlight-V1-ndk_platform.so': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
    (
        'vendor/lib/libwvhidl.so',
        'vendor/lib64/libwvhidl.so',
        'vendor/lib/mediadrm/libwvdrmengine.so',
        'vendor/lib64/mediadrm/libwvdrmengine.so',
    ): blob_fixup()
        .add_needed('libcrypto_shim.so'),
    (
        'vendor/lib/libiVptApi.so',
        'vendor/lib64/libiVptApi.so',
    ): blob_fixup()
        .add_needed('libiVptLibC.so'),
    (
        'vendor/lib/libiVptLibC.so',
        'vendor/lib/libHpEqApi.so',
        'vendor/lib64/libiVptLibC.so',
        'vendor/lib64/libHpEqApi.so',
    ): blob_fixup()
        .add_needed('libcrypto.so')
        .add_needed('libiVptHkiDec.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .add_needed('libinput_shim.so'),
}

module = ExtractUtilsModule(
    'pdx235',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
