import configparser

source=r'''<service>
  <id>JenkinsSlave</id>
  <name>Jenkins agent</name>
  <description>This service runs an agent for Jenkins automation server.</description>
  <executable>${JAVA}\java.exe</executable>
  <arguments>-Xrs -jar "%BASE%\agent.jar" -url ${URL} -secret ${SECRET} -name ${NAME} -workDir "${WORKDIR}"</arguments>
  <logmode>rotate</logmode>
  <onfailure action="restart" />
  <download from="${URL}/jnlpJars/agent.jar" to="%BASE%\agent.jar" />
 <extensions>
    <extension enabled="true" className="winsw.Plugins.RunawayProcessKiller.RunawayProcessKillerExtension" id="killOnStartup">
      <pidfile>%BASE%\jenkins_agent.pid</pidfile>
      <stopTimeout>5000</stopTimeout>
      <stopParentFirst>false</stopParentFirst>
    </extension>
  </extensions>
</service>
'''


conf = configparser.ConfigParser()
conf.read('../setting.ini', encoding='utf-8')
source = source.replace("${URL}", conf['SERVER']['url'])
source = source.replace("${SECRET}", conf['AGENT']['secret'])
source = source.replace("${NAME}", conf['AGENT']['name'])
source = source.replace("${WORKDIR}", conf['AGENT']['workdir'])
source = source.replace("${JAVA}", conf['ENV']['java'])

outfile = 'jenkins-slave.xml'
f = open(outfile, 'w')
f.write(source)

f.close()

print( source )
print(f'{outfile} generated!')

