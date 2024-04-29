#!/bin/bash
clear

echo "    _             _       ___           _        _ _ "
echo "   / \   _ __ ___| |__   |_ _|_ __  ___| |_ __ _| | |"
echo "  / _ \ | '__/ __| '_ \   | || '_ \/ __| __/ _' | | |"
echo " / ___ \| | | (__| | | |  | || | | \__ \ || (_| | | |"
echo "/_/   \_\_|  \___|_| |_| |___|_| |_|___/\__\__,_|_|_|"
echo ""

# ------------------------------------------------------
# Enter partition names
# ------------------------------------------------------
lsblk
read -p "Enter the name of the EFI partition: " efi
read -p "Enter the name of the ROOT partition: " root
read -p "Enter the name of the SWAP partition: " swap

# ------------------------------------------------------
# Sync time
# ------------------------------------------------------
timedatectl set-ntp true

# ------------------------------------------------------
# Format partitions
# ------------------------------------------------------
mkfs.fat -F 32 /dev/$efi
mkfs.ext4 -f /dev/$root
mkswap /dev/$swap
# ------------------------------------------------------
# Mount points
# ------------------------------------------------------
swapon /dev/$swap
mount /dev/$root /mnt
mount --mkdir /dev/$efi /mnt/boot/EFI
# ------------------------------------------------------
# Install base packages
# ------------------------------------------------------
pacstrap -K /mnt base base-devel git linux linux-firmware vim openssh intel-ucode
# ------------------------------------------------------
# Generate fstab
# ------------------------------------------------------
genfstab -U /mnt >>/mnt/etc/fstab
cat /mnt/etc/fstab
# ------------------------------------------------------
# Install configuration scripts
# ------------------------------------------------------
mkdir /mnt/archinstall
cp 2-configuration.sh /mnt/archinstall/
cp 3-yay.sh /mnt/archinstall/
cp 4-zram.sh /mnt/archinstall/
cp 5-timeshift.sh /mnt/archinstall/
cp 6-preload.sh /mnt/archinstall/
cp snapshot.sh /mnt/archinstall/

# ------------------------------------------------------
# Chroot to installed sytem
# ------------------------------------------------------
arch-chroot /mnt ./archinstall/2-configuration.sh
