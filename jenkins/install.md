# Install && Unstall


## MacOS 

### Inastll Way 1:
	brew install jenkins
	
	brew uninstall jekins
	
### Inastll Way 2: 
[Offical Download](https://jenkins.io/download/thank-you-downloading-osx-installer-stable)

	卸载 /Library/Application\ Support/Jenkins/Uninstall.command

### Running for way1

	安装完成即启动,默认 http://localhost:8080
	PC每次重启即自带启动jenkins
	
	启动 sudo launchctl load /Library/LaunchDaemons/org.jenkins-ci.plist
	停止 sudo launchctl unload /Library/LaunchDaemons/org.jenkins-ci.plist
	
### Running for way2

	启动 jenkins
	关闭 Control+C
	


