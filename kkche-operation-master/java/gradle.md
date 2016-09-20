
sudo add-apt-repository ppa:cwchien/gradle
sudo apt-get update
sudo apt-get install gradle

gradle tasks
gradle build
gradle wrapper

./gradlew tasks
./gradlew eclipse
./gradlew build
./gradlew run

vi build.gradle

```
apply plugin: 'maven'

repositories {
    maven {
        url "http://<hostname>:8081/nexus/content/groups/public"
        credentials {
            username '<userName>'
            password '<password>'
        }
    }
    mavenLocal()
    mavenCentral()
}
```
