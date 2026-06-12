If you're interviewing for a Linux System Administrator, Cloud Infrastructure Engineer, Platform Engineer, or Enterprise Linux Operations role, you should focus on SUSE Linux Enterprise Server (SLES) administration, architecture, patching, security, storage, networking, and automation.

## 1. What is SUSE Linux?

SUSE is one of the major enterprise Linux distributions alongside:

* Red Hat (RHEL)
* Canonical (Ubuntu)

Enterprise version:

* SUSE Linux Enterprise Server (SLES)

Community version:

* openSUSE

Common deployment environments:

* Datacenters
* VMware
* Cloud (AWS, Azure, GCP)
* SAP HANA environments
* High Availability Clusters

---

# 2. SUSE Architecture

Important directories:

| Directory | Purpose                       |
| --------- | ----------------------------- |
| /etc      | Configuration files           |
| /var      | Logs and application data     |
| /boot     | Bootloader files              |
| /home     | User home directories         |
| /tmp      | Temporary files               |
| /proc     | Kernel information            |
| /sys      | Hardware and kernel interface |

Useful commands:

```bash
hostnamectl
uname -r
cat /etc/os-release
uptime
free -h
df -h
lsblk
```

---

# 3. Package Management

One of the most common interview topics.

## Zypper

SUSE package manager:

```bash
zypper refresh
zypper update
zypper patch
zypper install nginx
zypper remove nginx
```

List repositories:

```bash
zypper repos
```

Add repository:

```bash
zypper ar <repo_url> custom_repo
```

Search package:

```bash
zypper search docker
```

Installed package:

```bash
rpm -qa | grep docker
```

### Difference Between Update and Patch

```bash
zypper update
```

Updates packages to latest versions.

```bash
zypper patch
```

Applies vendor-recommended security and bug-fix patches.

For production systems, administrators often prefer:

```bash
zypper patch
```

---

# 4. Service Management

SUSE uses systemd.

Check service:

```bash
systemctl status sshd
```

Start service:

```bash
systemctl start nginx
```

Enable at boot:

```bash
systemctl enable nginx
```

Restart:

```bash
systemctl restart nginx
```

View logs:

```bash
journalctl -u nginx
```

---

# 5. User Administration

Create user:

```bash
useradd john
passwd john
```

Create with home:

```bash
useradd -m john
```

Add to sudo group:

```bash
usermod -aG wheel john
```

Check groups:

```bash
id john
```

Lock account:

```bash
passwd -l john
```

---

# 6. Storage Management

Very common in enterprise interviews.

Check disks:

```bash
lsblk
fdisk -l
```

Create partition:

```bash
fdisk /dev/sdb
```

Create filesystem:

```bash
mkfs.xfs /dev/sdb1
```

Mount:

```bash
mount /dev/sdb1 /data
```

Persistent mount:

```bash
vi /etc/fstab
```

Example:

```bash
UUID=xxxx /data xfs defaults 0 0
```

Verify:

```bash
mount -a
```

---

# 7. LVM Administration

Interview favorite.

Check PV:

```bash
pvs
```

Create PV:

```bash
pvcreate /dev/sdb
```

Create VG:

```bash
vgcreate vg_data /dev/sdb
```

Create LV:

```bash
lvcreate -L 50G -n lv_app vg_data
```

Extend LV:

```bash
lvextend -L +20G /dev/vg_data/lv_app
```

Extend filesystem:

XFS

```bash
xfs_growfs /app
```

EXT4

```bash
resize2fs /dev/vg_data/lv_app
```

---

# 8. Networking

Show interfaces:

```bash
ip addr
```

Show routes:

```bash
ip route
```

Test connectivity:

```bash
ping
traceroute
```

Check ports:

```bash
ss -tulpn
```

DNS lookup:

```bash
dig google.com
nslookup google.com
```

Network config location:

```bash
/etc/sysconfig/network/
```

Interface configs:

```bash
/etc/sysconfig/network/ifcfg-*
```

Restart network:

```bash
systemctl restart network
```

---

# 9. Firewall

SUSE commonly uses firewalld.

Status:

```bash
firewall-cmd --state
```

Open port:

```bash
firewall-cmd --permanent --add-port=8080/tcp
```

Reload:

```bash
firewall-cmd --reload
```

List rules:

```bash
firewall-cmd --list-all
```

---

# 10. Process Management

View processes:

```bash
ps -ef
```

Interactive view:

```bash
top
```

or

```bash
htop
```

Kill process:

```bash
kill -9 PID
```

Find process:

```bash
pgrep java
```

---

# 11. Log Management

System logs:

```bash
journalctl
```

Kernel logs:

```bash
journalctl -k
```

Boot logs:

```bash
journalctl -b
```

Follow logs:

```bash
journalctl -f
```

Traditional logs:

```bash
/var/log/messages
```

---

# 12. SUSE Security

Check SELinux:

```bash
getenforce
```

SUSE usually uses:

### AppArmor

Status:

```bash
aa-status
```

Restart:

```bash
systemctl restart apparmor
```

Key interview point:

> Unlike RHEL which primarily uses SELinux, SUSE commonly uses AppArmor for mandatory access control.

---

# 13. SUSE Registration

Enterprise systems need registration.

Check registration:

```bash
SUSEConnect --status-text
```

Register system:

```bash
SUSEConnect -r <registration-code>
```

List extensions:

```bash
SUSEConnect --list-extensions
```

---

# 14. Kernel Management

Current kernel:

```bash
uname -r
```

Installed kernels:

```bash
rpm -qa | grep kernel
```

Bootloader:

```bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

---

# 15. High Availability (Frequently Asked)

SUSE is widely used for HA clusters.

Components:

* Pacemaker
* Corosync
* Fencing (STONITH)

Check cluster:

```bash
crm status
```

Cluster resources:

```bash
crm configure show
```

Typical use cases:

* SAP HANA
* Databases
* Critical applications

---

# 16. Automation with Ansible

Since your background includes Ansible and infrastructure automation, be prepared for questions like:

### Install package

```yaml
- name: Install nginx
  zypper:
    name: nginx
    state: present
```

### Start service

```yaml
- name: Start nginx
  service:
    name: nginx
    state: started
    enabled: yes
```

### Patch server

```yaml
- name: Patch SLES server
  zypper:
    name: '*'
    state: latest
```

---

# 17. Common Interview Scenarios

### Disk Full

Check:

```bash
df -h
du -sh /*
find / -type f -size +1G
```

### Server Slow

Check:

```bash
top
vmstat 5
iostat -x 5
sar
```

### Service Down

```bash
systemctl status service
journalctl -u service
ss -tulpn
```

### Network Issue

```bash
ip addr
ip route
ping gateway
nslookup
```

---

# 18. Questions You May Be Asked

### What is zypper?

SUSE's package management tool used to install, update, patch, and manage repositories.

### Difference between zypper update and zypper patch?

* update → updates packages
* patch → applies vendor security and bug-fix patches

### What security framework does SUSE use?

AppArmor.

### How do you extend an LVM filesystem?

1. Add disk
2. pvcreate
3. vgextend
4. lvextend
5. xfs_growfs or resize2fs

### How do you troubleshoot a service not starting?

1. systemctl status
2. journalctl -xe
3. Check ports
4. Check permissions
5. Verify dependencies

---

## 30-Second Interview Introduction

> "I have experience administering enterprise Linux environments, including RHEL and SUSE Linux. My responsibilities include server provisioning, patch management using zypper, user and access management, LVM administration, troubleshooting services, networking, security hardening with AppArmor, automation using Ansible, and supporting infrastructure across VMware and cloud platforms. I also work with CI/CD and Infrastructure as Code tools such as Terraform and Jenkins, which helps automate Linux operations at scale."

This introduction aligns well with Cloud Infrastructure Engineering, Platform Engineering, and Linux Enterprise Operations roles.

zypper :
| Command         | What It Does                                   |
| --------------- | ---------------------------------------------- |
| `zypper patch`  | Installs vendor-recommended patches            |
| `zypper update` | Updates packages to latest repository versions |

Commands Often Used Together
zypper refresh
zypper list-patches
zypper patch --dry-run
zypper patch