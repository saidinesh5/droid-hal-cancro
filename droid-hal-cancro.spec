# These and other macros are documented in dhd/droid-hal-device.inc
%define device cancro
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 3/Mi 4
%define installable_zip 1
%define straggler_files \
/init.class_main.sh\
/init.mdm.sh\
/init.qcom.class_core.sh\
/init.qcom.early_boot.sh\
/init.qcom.factory.sh\
/init.qcom.sh\
/init.qcom.ssr.sh\
/init.qcom.syspart_fixup.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

#For OTA
%define enable_kernel_update 1

%include rpm/dhd/droid-hal-device.inc
