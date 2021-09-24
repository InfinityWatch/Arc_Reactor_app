Initial Triage - Jarvis Host Analysis - Utilizes saved searche IOC's within the MITRE ATTACK framework. 
THE WHITELISTS Tab will only affect the Jarvis DASHBOARD!
![Initial Triage Jarvis](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Initial%20Triage%20Jarvis%20Host.PNG)

Summary Indexes - The summary indexes feed information into the Jarvis Host Dashboard - Go under Settings - Indexes and verify the host_jarvis_summary index is there.
![https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/jarvis%20summary%20index.PNG)

Getting Rid of old indexed data in summary index ( host_jarvis_summary) - splunk clean eventdata -index <index_name>
![Initial Triage Jarvis](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/jarvis-%20clean%20index.PNG)

Jarvis Whitelist - The Whitelist tab is assosiated to the jarvis host dashboard. The Whitelist dashboards are saved as csv files. Go under Settings - Lookup - Lookup Table Files. 
![Jarvis Whitelist]https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/jarvis%20whitelist.PNG)

Jarvis Saved Searches - Because of the resource intense nature, all saved searches are turned off. To turn on all saved searches at the same time,
located the saved search file under /opt/splunk/etc/apps/Arc_reactor_app/default/savedsearches.conf. Utilizing vim . . . you can edit all lookups
with replacing the enabled Sched = 1, ensure dispatch.earliest and dispatch.latest are set appropriately, and the `indextime` macro assosiated in the search query is set as 
shown in the next picture.
![Initial Triage Jarvis](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Jarvis%20-%20saved%20searches.PNG)

Jarvis Macros - Verifying the indextime macro is set appropriately is important to get the correct results into the host jarvis summary dashboard. To verify settings go to 
Settings - Advanced Settings , Search macros for `indextime`. Verify all windows macros and the sysmon macro are set to the correct indexes as well.
![Initial Triage Jarvis](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Jarvis%20macros.PNG)
