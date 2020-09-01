# Parameters to modify
declare -a arr=("v1.1.0" "v1.2.36" "v1.2.51" "v1.2.5" "v1.2.6" "v1.2.8" "v1.2.9")
download_path="/../../Downloads/"
project_name="apkname"
sink_folder="/../Documents../../"
# If XAPK you should identify and write the main package apk
main="com.gov.example.apk"

for i in "${arr[@]}"
do
  echo "$i"
  version="$i"
  mkdir -p $sink_folder$project_name/$version
  xapk="Name of the app"$i"_apkpure.com.xapk"
  apk="Name of the app_"$i"_apkpure.com.apk"

  if [[ -f $download_path$xapk ]];
  then
    echo $xapk
    unzip "$download_path$xapk" -d $sink_folder$project_name/"$i"/
    cp $sink_folder$project_name/"$i"/$main $sink_folder$project_name/"$i"/$project_name.apk
  elif [[ -f $download_path$apk ]];
  then
    echo $apk
    cp "$download_path$apk" $sink_folder$project_name/"$i"/$project_name.apk

  fi
  apktool d -o $sink_folder$project_name/"$i"/$project_name $sink_folder$project_name/"$i"/$project_name.apk
done
