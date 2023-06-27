Name: display-commonsys-intf-linux
Version: 1.0
Release: r0
Summary: install commonsys-intf-display headers
Source0: %{name}-%{version}.tar.gz
License: BSD-3-Clause


%description
This contains opensource headers files for commonsys-intf-display

%prep
%setup -qn %{name}

%install
mkdir -p %{buildroot}%{_includedir}
cp color_metadata.h %{buildroot}%{_includedir}
cp smomo_interface.h %{buildroot}%{_includedir}


%files
%{_includedir}/color_metadata.h
%{_includedir}/smomo_interface.h

