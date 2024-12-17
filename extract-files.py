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
    'hardware/qcom-caf/sm8450',
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
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    # TODO fix these better
    'vendor/lib/libmmrtpdecoder_proprietary.so': blob_fixup().replace_needed('libmmosal.so', 'libmmosal_vendor.so'),
    'vendor/lib/libmmrtpencoder_proprietary.so': blob_fixup().replace_needed('libmmosal.so', 'libmmosal_vendor.so'),
    'vendor/lib/libwfduibcsink_proprietary.so': blob_fixup().replace_needed('libmmosal.so', 'libmmosal_vendor.so'),
    'vendor/lib/libwfdmminterface_proprietary.so': blob_fixup().replace_needed('libmmosal.so', 'libmmosal_vendor.so'),
    'vendor/lib/libFileMux_proprietary.so': blob_fixup().replace_needed('libmmosal.so', 'libmmosal_vendor.so'),
    'vendor/lib/libwfdmmservice_proprietary.so': blob_fixup().replace_needed('libmmosal.so', 'libmmosal_vendor.so'),

    'vendor/lib64/libdpmqmihal.so': blob_fixup().replace_needed('com.qualcomm.qti.dpm.api@1.0.so', 'com.qualcomm.qti.dpm.api@1.0_vendor.so'),
    'vendor/bin/dpmQmiMgr': blob_fixup().replace_needed('com.qualcomm.qti.dpm.api@1.0.so', 'com.qualcomm.qti.dpm.api@1.0_vendor.so'),

    'vendor/lib/vendor.qti.imsrtpservice@3.0-service-Impl.so': blob_fixup().replace_needed('vendor.qti.imsrtpservice@3.0.so', 'vendor.qti.imsrtpservice@3.0_vendor.so'),
    'vendor/lib64/vendor.qti.imsrtpservice@3.0-service-Impl.so': blob_fixup().replace_needed('vendor.qti.imsrtpservice@3.0.so', 'vendor.qti.imsrtpservice@3.0_vendor.so'),
    'vendor/lib64/lib-imsvtcore.so': blob_fixup().replace_needed('vendor.qti.imsrtpservice@3.0.so', 'vendor.qti.imsrtpservice@3.0_vendor.so'),
    'vendor/lib64/vendor.qti.data.factory@2.0.so': blob_fixup().replace_needed('vendor.qti.ims.rcsconfig@1.0.so', 'vendor.qti.ims.rcsconfig@1.0_vendor.so'),

    'system_ext/lib/libwfdservice.so': blob_fixup().replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V3-cpp.so'),
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
