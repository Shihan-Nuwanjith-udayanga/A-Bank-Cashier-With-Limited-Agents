# A-Bank-Cashier-With-Limited-Agents

Installed Libries
-----------------
<b>SimPy</b>	- The main simulation framework for event-based modeling (used to create the bank simulation). <br>
<b>NumPy</b>	- Used for mathematical operations, random sampling, and data processing. <br>
<b>Matplotlib</b>	- Used for plotting and visualizing results (charts, graphs). <br>
<b>Pandas</b>	- Helps manage and analyze tabular data (e.g., results, summaries, CSV files). <br>

This Code Does
--------------
<b>Simulates</b> customers arriving at a bank with limited cashiers <br><br>
<b>Measures:</b> Waiting time per customer, Service duration and Cashier utilization (how busy the agents are) <br><br>
<b>Generates three charts:</b> <br>
<b>1.Wait Time per Customer</b> – shows individual waiting times<br>
<b>2.Wait Time Histogram</b> – shows overall distribution of delays<br>
<b>3.Cashier Utilization</b> Pie Chart – shows how much time cashiers were busy vs idle<br>

How to Run this Code
--------------------
python src/case_study/app.py

Install prerequisites
---------------------
<b>Install Python in Your Computer</b> <br><br>
<b>Create a Virtual Environment</b> <br>
Run this command to create an isolated environment: <br>
<\t>python -m venv .venv<br><br>
<b>Active it</b><br>
<b>Windows (CMD)</b><br>
<\t>.venv\Scripts\activate<br><br>
<b>Install Required Packages</b><br>
With your virtual environment active, install dependencies:<br>
pip install --upgrade pip<br>
pip install simpy numpy matplotlib pandas





