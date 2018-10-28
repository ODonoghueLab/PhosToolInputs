# Input files

Provided in this repository are input files required for the various tools.


<table> 
	<tr>
		<th> File name 
		</th>
		<th> Comment
		</th>
		<th> Tool link 
		</th>
	</tr>
	<tr> 
		<td> 
			DiBS/Dibsvis.csv 
		</td>
		<td> 
			Csv file input file for use with the DiBS tool 
		</td>
		<td> 
			<a href="http://www.dibsvis.com">DiBS</a>
		</td>
	</tr>
	<tr> 
		<td> 
			DynaPho/Dynapho.txt
		</td>
		<td> 
			Tab separated file for use with the DynaPho tool 
		</td>
		<td> 
			<a href="http://140.112.52.89/dynapho/"> DynaPho web tool </a>
		</td>
	</tr>
	<tr> 
		<td> 
			<ol> 
				<li> PhosphoPath/PhosphoPath_network.txt </li>
				<li> PhosphoPath/PhosphoPath_timeseries.txt </li>
			</ol>
		</td>
		<td> 
			<ol>
				<li> Tab separated file for proteins and their sites </li>
				<li> Tab separated file for the quantified values at various time points </li>
			</ol>
		</td>
		<td> 
			<a href="http://www.cytoscape.org"> Cytoscape tool </a>, <a href="http://apps.cytoscape.org/apps/phosphopath"> PhosphoPath plugin </a>
		</td>
	</tr>
	<tr> 
		<td> 
			Phoxtrack/Phoxtrack.txt
		</td>
		<td> 
			Tab separated file for use with the PHOXTRACK tool
		</td>
		<td> 
			<a href="http://phoxtrack.molgen.mpg.de"> PHOXTRACK web tool </a>
		</td>
	</tr>
	<tr> 
		<td>
			Kappa/InsulinSignallingModel.ka 
		</td>
		<td> 
			Basic insulin signalling model in kappa format 
		</td>
		<td> 
			<a href="https://tools.kappalanguage.org/try/?model=https%3A//raw.githubusercontent.com/Kappa-Dev/KaSim/master/models/abc-pert.ka"> Kappa online tool </a>, 
			<a href="https://kappalanguage.org"> Kappa language home page </a>
		</td>
	</tr>
</table>
	

## Additional files

<table> 
	<tr>
		<th> File name 
		</th>
		<th> Comment
		</th>
	</tr>
	<tr>
		<td> Original.txt
		</td>
		<td> Original data points from Humphrey <i> et al. </i> [1].
		</td>
	</tr>
	<tr>
		<td> getTpPhosData.py, phosphopath_input.tab
		</td>
		<td> Python and an input file, to re-generate PhophoPath_timeseries.txt. 
		</td>
	</tr>
</table>


The python script can be run as: 

```python3 getTpPhosData.py phosphopath_input.tab > PhophoPath_timeseries.txt```


