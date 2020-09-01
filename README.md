# APK permissions Analysis

The code on this repository allows the user to analyze the permissions of an android application.
**Extracting the permissions list and comparing against different apk versions of
the same application** to get a global view about the permissions used over the time in different versions of the application.

# Pre-requirement


- You need to have [apktool](https://ibotpeaches.github.io/Apktool/]) or another tool to decompile the apk's
- Python 3 to execute the code present on this repository

# How it works

Before all you have to clone the repository

```
  git clone https://github.com/karisma-klab/analisis-permisos-apk.git
  cd analisis-permisos-apk
```
To use it is really simple.
- First you should have the apk's that you want to analyze.
- Second, you can use the script under the utils folder `utils/apk_coordinator.sh` to create the good folders structure used by the code.
- Last create a python script that uses the APKAnalyzer class as on the `example.py` file. That will generate the permissions x versions matrix on the desired format.


# Usage example
We want to analyze the android application "gamma101".

We have already downloaded the apk versions that we want to analyze to the following directory:
```
└── Downloads
    ├── gamma101_v2.0.5_apkpure.com.apk
    ├── gamma101_v2.0.7_apkpure.com.apk
    └── gamma101_v2.1.2_apkpure.com.apk
```
So we modify the bash script `apk_coordinator.sh` with the following values:
```
declare -a arr=("v1.1.0" "v1.2.36" "v1.2.51" "v1.2.5" "v1.2.6" "v1.2.8" "v1.2.9")
download_path="<full_path>/../Downloads/"
project_name="gamma101"
sink_folder="/../Documents../../Project001"
```

**Warning: here you should have already installed apktool because is used by the bash script to decompile the apk**

After executing the bash script we obtain the following directories structure at the sink folder location:
```
└── Project001
    └── gamma101
        ├── v2.0.5
        │   └── gamma101
        │       └── AndroidManifest.xml
        │       └── ...
        │       └── ...
        ├── v2.0.7
        │   └── gamma101
        └── v2.1.2
            └── gamma101
```

Finally, we create python code as following:

```
from apk_perms_analyzer import APKAnalyzer

apk_versions = ["v2.0.5", "2.0.7", "2.1.2"]

analyzer = APKAnalyzer()

analyzer.apk_permission_analysis("gamma101", apk_versions, "/../Documents../../Project001")
```

After execute it you will obtain the permissions comparison matrix between the different apk versions.
