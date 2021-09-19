# Arc_Reactor_app
Splunk app with default datamodels and dashboards for Windows Events, Sysmon, and Zeek logs. Also includes a MITRE ATTACK Framework incident management dashboard and other helpful views.

Home Page: The Home overview is to be utilzed for verified incidents that are framed and categorized by the MITRE ATTACK Framework. Inputing incidents are completed under the Home tab - Annolyst Annotations dashboard. Dependencies for this dashboard are analyst_annotations.csv and mitre_attack_framework.csv lookup files.
![Home Overview](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Home-overview.PNG)

Home - Network Monitoring: Network Monitoring will show all network injested data and quick visualizations.
![Network Monitoring](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/home-network-monitoring.PNG)

Home -Network Map is to show a visual representation of the network that is being monitored. There are 3 example lookup table files (Network Map, Network Map2, Frothly) that are currently in the dashboard as examples. Dependencies for this dashboard are the lookup file for the Network Map and Network Diagram Viz app.
![Home Network Map](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/home-network%20map.PNG)

Network Map Example 2:
![Home Network Map](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/home-network%20map%202.PNG)

Home - Analyst Annotation Maker is used to feed information to the Home overview page. A useful but not dependant app to have is the Lookup Editor App.
![Home Analyst Annotation](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/home-analyst%20annotation.PNG)

Home - Analyst Viewer will show all events logged by analyst's from the Analyst Annotation maker tab.
![Home Analyst Viewer](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/home-analyst%20annotation%20viewer.PNG)

Host - Sysmon Overview dashboard is useful to see highlights of injested data. As seen in the bottom left and bottom right panels, All clickable events (Computer Clickable and User Clickable) will be identified and pushed to the correct drilldown.
![Host Sysmon](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Host-Sysmon.PNG)

Example Computer Drilldown when clicked on from Sysmon overview computer clickable panel. 
![Host Systmon Computer Drilldown](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Host-Sysmon%20-%20Computer%20Drilldown%20Pivot.PNG)

Host - TSTATS Sysmon is a replica of the TSTATS overview. In terms of speed, TSTATS dashboards will be much faster. No TSTATS dashboards have objects that are clickable to drilldowns. 
![Host Sysmon TSTATS](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Host-Sysmon%20TSTATS.PNG)

Host - Windows Events Summary Dashboard example:
![Home Windows Computer Clickable](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Host-Windows%20Events%20Computer%20clickable.PNG)

Network - Zeek - Zeek Conn example. can be filtered by choices shown:
![Network Zeek Conn](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Network%20-%20Zeek%20Conn.PNG)

Network - Zeek - Zeek SSL and X509 example: Dependencies for this dashboard are for the Ja3 Panels that utilze the ja3_json indexed data. The ja3_json data will need to be updated regularly.
![Network Zeek SSL and Ja3](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Network%20-%20Zeek%20SSL.PNG)

Network - 
![Network Zeek SRC and DEST lookup TSTATS](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Network%20-%20Zeek%20TSTATS%20search%20by%20SRC%20DEST.PNG)

![Network Zeek src and dest ip lookup](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Network%20-%20easy%20IP%20search.PNG)

![Drilldowns](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Drilldowns%20-%20Computer%20Overview%20-%20Tabs.PNG)

![Initial Triage Intel Keyword](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Initial%20Triage%20Intel%20keyword.PNG)

![Initial Triage Network Anamolies](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Initial%20Triage%20Network%20Anomalies.PNG)

![Initial Triage Suricata](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Initial%20Triage%20Suricata.PNG)

![Whitelist Editor](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Whitelest%20Editor.PNG)

![Splunk](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Splunk%20-%20Alerts.PNG)

![FRIDAY About](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/FRIDAY%20-%20About.PNG)

![FRIDAY Sourcetypes Metadata](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/FRIDAY%20-%20Sourcetypes%20Metadata.PNG)

![FRIDAY Splunk Stats](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/FRIDAY%20-%20Splunk%20Stats.PNG)

