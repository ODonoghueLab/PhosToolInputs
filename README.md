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
		<td> Original 103 profiles from Humphrey <i> et al. </i> [1].
		</td>
	</tr>
	<tr>
		<td> PhosphoPath/getTpPhosData.py, Phosphopath/phosphopath_input.tab
		</td>
		<td> Python script and input file, respectively, to re-generate PhophoPath_timeseries.txt. 
		</td>
	</tr>
	<tr>
		<td> Kinase_assignments.xlsx
		</td>
		<td> Excel file containing the kinase assignments, where known, for the 103 profiles [1,2].
		</td>
	</tr>
</table>


The python script can be run as: 

```python3 getTpPhosData.py phosphopath_input.tab > PhophoPath_timeseries.txt```


## References

1. Humphrey SJ, Yang G, Yang P, Fazakerley DJ, Stöckli J, Yang JY, James DE. Dynamic adipocyte phosphoproteome reveals that Akt directly regulates mTORC2. Cell metabolism. 2013 Jun 4;17(6):1009-20.
2. Ma DK, Stolte C, Krycer JR, James DE, O’Donoghue SI. SnapShot: insulin/IGF1 signaling. Cell. 2015 May 7;161(4):948.


