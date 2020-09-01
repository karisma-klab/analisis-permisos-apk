import os
import csv
from distutils.version import LooseVersion
import xml.etree.ElementTree as ET
import filecmp
import json
from pathlib import Path


class APKAnalyzer():
    def __init__(self):
        self.file = "AndroidManifest.xml"
    def get_permission(self, path):
        """Parse and exract the permissions of a given AndroidManifest.xml file.

        Args:
            path (str): Path to the AndroidManifest.xml file.

        Returns:
            permission_list: A list containing the list of permissions of an
            application descriptor.
        """
        root = ET.parse(path).getroot()
        permissions = root.findall("uses-permission")
        permissions_list = []
        for permission in permissions:
            for attribute in permission.attrib:
                permissions_list.append((attribute, permission.attrib[attribute]))
        permission_list = [s.split('.')[-1] for j,s in permissions_list]
        return permission_list

    def apk_permission_analysis( self, apk_name, versions, root_dir, generate_csv=False, csv_path="" ):
        """Process the permission of one or more file to generate a sorted
        permissions x versions matrix as csv or as print it as stdout.

        Args:
            apk_name (str): APK Name where dir where are placed the APK's.
            versions (list[str]): A list of apk versions corresponding to the
            directories where are placed the decompiled APK's
            root_dir (str): parent path of the apk folder
            For example if apk_name=dummyapk and versions=[1.0.0,1.0.1] the
            following directories structure should exist:
            - root_dir
            ---- apk_name
            -------- v1.0.0
            ------------ apk_name
            ---------------- decompiled apk files
            -------- v1.0.1
                             ...

        Returns:
            permission_list: A list containing the list of permissions of an
            application descriptor.
        """
        versions = sorted(versions, key=LooseVersion)
        root_path = os.path.join(root_dir, apk_name)
        perms_per_version = {}

        for version in versions:
            manifest_path = os.path.join(root_path,"v{}".format(version), apk_name, self.file)
            plist = self.get_permission(manifest_path)
            plist_set = list(set(plist))
            for permission in plist_set:
                if permission not in perms_per_version:
                    perms_per_version[permission] = []
                perms_per_version[permission].append(version)

        rows = []

        for permission in sorted(perms_per_version.keys()):
            row_string = permission
            rw = []
            rw.append(permission)
            for version in versions:
                if version in perms_per_version[permission]:
                    rw.append("x")
                else:
                    rw.append("-")
            rows.append(rw)

        if generate_csv is True:
            with open(csv_path+apk_name+'.csv', 'w', newline='') as csvfile:
                sw = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                sw.writerow(["PERMISSION_NAME"]+versions)
                for row in rows:
                    sw.writerow(row)
        else:
            print(["PERMISSION_NAME"]+versions)
            for row in rows:
                print(row)
