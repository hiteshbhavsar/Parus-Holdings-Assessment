# Parus-Holdings-Assessment
This repository contains code for Parus Holdings Assessment
<br>
## Description of the problem statement
The problem given was that given the list of all items and the given target price. I need to find all the possible combinations of dishes. The input for the data would be taken using a json file. To learn more about the requirements click the link given [here](https://docs.google.com/document/d/1-h-mZy5jjyC4Hu2vIaQHnW1ptOygl7ZhC0K8pWIPU7o/edit#heading=h.g4a4qafh8shy).
<br>
## Input format to be followed
Sample input data
<blockquote>
Target price, $15.05

mixed fruit,$2.15
french fries,$2.75
side salad,$3.35
hot wings,$3.55
mozzarella sticks,$4.20
sampler plate,$5.80

</blockquote>
<code>
{
	"Target Price":15.05,
	"items":[
		{
			"Name":"Mixed Fruit",
			"Price":2.15
		},
		{
			"Name":"french Fries",
			"Price":2.75
		},
		{
			"Name":"side salad",
			"Price":3.35
		},
		{
			"Name":"Hot Wings",
			"Price":3.55
		},
		{
			"Name":"mozzorella sticks",
			"Price":4.20
		},
		{
			"Name":"Sampler plate",
			"Price":5.80
		}
	]
}
</code>
<br>

## Steps for execution of program through command line parameters using command prompt
<ol>
  <li>Unzip the folder of code (Provided you have downloaded the code in zip format)</li>
  <li>Open Command Prompt and change the directory to the current directory using <code> cd current_directory </code> command</li>
  <ol>
    <li>Here current_directory means the place where the code is saved</li>
    <li> <i>For Example </i> <code>cd "F:\Python Projects\Parus Holdings"</code>
  </ol>
  <li>Run the command <code>python project.py <b>file_name</b></code></li>
  <li>The above code can be written in two formats.
  <ol>
    <li>By directly mentioning the file in the same directory to read from. <i>For Example</i> <code>python project.py input.json</code></li>
    <li> By directly mentioning the file path to read from <i>For Example</i> <code>python project.py "F:\Python Projects\Parus Holdings\input.json"</code></li>
  </ol>
	<li>If its getting difficult to understand the steps mentioned above then kindly download the [file](https://github.com/hiteshbhavsar/Parus-Holdings-Assessment/blob/main/Steps%20to%20follow%20to%20run%20the%20code.docx)</li>
</ol>
