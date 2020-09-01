from apk_perms_analyzer import APKAnalyzer

apk_versions = ["1.0.0", "1.0.2", "1.0.4", "1.0.5", "1.0.9", "1.0.11", "2.0.0", "2.0.1", "2.0.3", "2.0.4", "2.0.5"]

analyzer = APKAnalyzer()

analyzer.apk_permission_analysis("<apk_name>", apk_versions, "/home/.../../")
