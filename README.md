# Summary
This ControlScript can be used to enable or disable traffic to an Avi Virtual Service with an accompanying alert trigger.

# Configuration Steps
Create a ControlScript under Templates > Scripts > ControlScripts. Import main.py from this repository or copy and paste the text, then click Save.

<img src="images/Create_ControlScript.png" width="400">

Create an Alert Action under Operations > Alert Actions to fire the ControlScript.

<img src="images/Create_Alert_Action.png" width="400">

Create Alert Config under Operations > Alert Config which will associate a particular event to the Alert Action. This ControlScript looks for "VIP_UP" and "VIP_DOWN" Alerts.

<img src="images/Create_Alert_Configuration.png" width="400">

# Testing / Validation

Using a test virtual service that is in a working state, verify that the Traffic Enabled knob is turned on.

<img src="images/Verify_Traffic_Enabled_On.png" width="400">

Disable the pool associated with the virtual service

<img src="images/Pool_Disabled.png" width="400">

Wait for the alert to fire. During testing this could take up to 2 minutes. The alert can be viewed under Operations > All Alerts. Note the logs of the alert will detail which virtual service the ControlScript updated and to what value the traffic_enabled attribute was set.

<img src="images/Alert_Fired.png" width="600">

Verify that the traffic enabled attribute has been updated

<img src="images/Traffic_Enabled_False.png" width="400">

Enable the pool associated with the virtual service

<img src="images/Pool_Enabled.png" width="400">

Wait for the alert to fire again.

<img src="images/Alert_Fired_VIP_UP.png" width="600">

Verify that the traffic enabled attribute has updated accordingly.

<img src="images/Traffic_Enabled_True.png" width="400">