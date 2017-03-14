# rpm_device is the name of the ported device
%define rpm_device tate
# rpm_vendor is used in the rpm space
%define rpm_vendor amazon

# Manufacturer and device name to be shown in UI
%define vendor_pretty Amazon
%define device_pretty Kindle Fire HD 7

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 0

%include droid-hal-version/droid-hal-version.inc
