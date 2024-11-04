wget https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
tar -xzf openjdk-11.0.2_linux-x64_bin.tar.gz
export JAVA_HOME=$PWD/jdk-11.0.2
export PATH=$JAVA_HOME/bin:$PATH
