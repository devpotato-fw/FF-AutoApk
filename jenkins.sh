# 指定编译目录
path='./app/'
file_app_path=${path}src/main/java/com/example/test/AppEnv.java

# 配置蒲公英KEY
api_key="1342d4dd949c1bc97e9bfdf42ac77b78"

# 配置蒲公英更新描述信息
pgyer_desc="Test新包"

# 更改打包环境
environment="SRERVICE_ENVIRONMENT"
target_environment=${nameSuffix}

sed -i '' 's/'${environment}'/'${target_environment}'/g' $file_app_path

# 打包
echo "exporting..."
./gradlew assembleRelease

#上传蒲公英
echo "uploading..."
apk="./app/build/outputs/apk/release/app-release.apk"
curl -F 'file=@'${apk} -F '_api_key='${API_KEY} -F 'buildUpdateDescription='${PGYER_DESC} https://www.pgyer.com/apiv2/app/upload
echo -e "\n** UPLOAD TO PGYER SUCCEED **\n"

# 更改打包环境
sed -i '' 's/'${target_environment}'/'${environment}'/g' $file_app_path