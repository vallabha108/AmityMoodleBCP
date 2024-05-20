current_datetime=$(date +"%Y-%m-%d %T")
current_date=$(date +"%Y-%m-%d")

#Loggin
echo "Zip Process Started: $current_datetime" >> /root/logs/timing.txt

#ZipFile
zip_file="/root/elearningData_$current_date.zip"
zip -r "$zip_file" /home/amityacu/moodledata2


current_datetime=$(date +"%Y-%m-%d %T")
echo "Zip Process Ended: $current_datetime" >> /root/logs/timing.txt

current_datetime=$(date +"%Y-%m-%d %T")
echo "Upload Process Started: $current_datetime" >> /root/logs/timing.txt

python3 /root/BKP_Scripts/upload_file.py "$zip_file"


current_datetime=$(date +"%Y-%m-%d %T")
echo "Upload Process Ended: $current_datetime" >> /root/logs/timing.txt

rm "$zip_file"

