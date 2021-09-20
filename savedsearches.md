Searches Reports and Alerts - 154 alerts are to many to look through individually but for a quick glance this is where from a GUI perspective all searches are located. Because of search resources, 95% of all searches are turned off. Below shows where to turn all of the searches on at once instead of individually clicking each search.
![Searches and Reports](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/Searches%20and%20Reports.PNG)

All searches can be found under Arc_reactor_app/default/savedsearches.conf
![From Command Line](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/savedsearches%20-%20from%20cmd.PNG)

Saved Searches - cron_schedule and enableSched: 
Cron Scdedule is currently set to run once a day at midnight in this example. Please see Splunk documentation to change. 
Enable_sched is set to 0 or false. Set to 1 if you want the 
![Time Run and Enabled](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/savedsearches%20-%20time%20run%20and%20enabled.PNG)

indextime macro sets the control for the time range of the seach. Currently it is set to all time. Change and find the macro in advance search - macros. 
![Index Time macro](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/savedsearch%20-%20index%20time.PNG)

Summary Index - Collect exemplifies taking the results and saving the results into a different index. This index needs to be created in order for the search to work correctly. Check indexes for host_jarvis_summary in indexes as shown in the example below.
![Summary Index Used](https://github.com/InfinityWatch/Arc_Reactor_app/blob/main/pictures/savedsearches%20-%20summary%20index.PNG)
