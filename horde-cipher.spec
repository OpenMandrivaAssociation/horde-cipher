%define prj    Horde_Cipher

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-cipher
Version:       0.0.2
Release:       %mkrel 3
Summary:       Secret Encryption API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
The Secret:: class provides an API for encrypting and decrypting small
pieces of data with the use of a shared key.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Cipher
%dir %{peardir}/Horde/Cipher/BlockMode
%{peardir}/Horde/Cipher.php
%{peardir}/Horde/Cipher/BlockMode.php
%{peardir}/Horde/Cipher/BlockMode/cbc.php
%{peardir}/Horde/Cipher/BlockMode/cfb64.php
%{peardir}/Horde/Cipher/BlockMode/ecb.php
%{peardir}/Horde/Cipher/BlockMode/ofb64.php
%{peardir}/Horde/Cipher/blowfish.php
%{peardir}/Horde/Cipher/cast128.php
%{peardir}/Horde/Cipher/des.php
%{peardir}/Horde/Cipher/rc2.php
%{peardir}/Horde/Cipher/rc4.php
%dir %{peardir}/tests/Horde_Cipher
%dir %{peardir}/tests/Horde_Cipher/tests
%{peardir}/tests/Horde_Cipher/tests/Cipher1.phpt
%{peardir}/tests/Horde_Cipher/tests/Cipher2.phpt
%{peardir}/tests/Horde_Cipher/tests/Cipher3.phpt
%{peardir}/tests/Horde_Cipher/tests/Cipher4.phpt
%{peardir}/tests/Horde_Cipher/tests/Cipher5.phpt
%{peardir}/tests/Horde_Cipher/tests/Cipher6.phpt

