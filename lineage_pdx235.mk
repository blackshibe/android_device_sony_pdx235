#
# Copyright (C) 2018 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from device.mk
$(call inherit-product, $(LOCAL_PATH)/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

IS_PHONE := true

PRODUCT_BUILD_PROP_OVERRIDES := \
    DeviceName=XQ-DC72 \
    DeviceProduct=XQ-DC72 \
    SystemDevice=XQ-DC72 \
    SystemName=XQ-DC72 \
    BuildFingerprint=Sony/XQ-DC72/XQ-DC72:14/68.1.A.2.270/068001A002027000521798587:user/release-keys \
    BuildDesc="XQ-DC72-user 14 68.1.A.2.270 068001A002027000521798587 release-keys"

PRODUCT_NAME := lineage_pdx235
PRODUCT_DEVICE := pdx235
PRODUCT_MANUFACTURER := Sony
PRODUCT_BRAND := Sony
PRODUCT_MODEL := XQ-DC72

PRODUCT_SYSTEM_NAME := XQ-DC72
PRODUCT_SYSTEM_DEVICE := XQ-DC72

PRODUCT_GMS_CLIENTID_BASE := android-sonymobile