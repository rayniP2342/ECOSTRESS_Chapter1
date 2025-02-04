# ECOSTRESS Literature Review

This document summarizes findings from various papers relating to ECOSTRESS.

## Template for New Papers

```markdown
### [Author Last Name] et al., [Year]

**Title:** *[Paper Title]*

**Authors:** [List of Authors]

**Year:** [Year]

**DOI:** [Link to DOI or URL]

**Findings:** 
- [Point 1]
- [Point 2]
- [Point 3]
...
**Additional Notes:**
- [Optional extra information]
```

### Nicholson et al., 2021

**Title:** *Evaluation of a CONUS-Wide ECOSTRESS DisALEXI Evapotranspiration Product*

**Authors:** Cawse-Nicholson, K., Anderson, M. C., Yang, Y., Yang, Y., Hook, S. J., Fisher, J. B., Halverson, G., Hulley, G. C., Hain, C., Baldocchi, D. D., Brunsell, N. A., Desai, A. R., Griffis, T. J., & Novick, K. A. 

**Year:** 2021

**DOI:** https://doi.org/10.1109/JSTARS.2021.3111867

**Findings:** 
This study uses eddy flux tower data to validate the ECOSTRESS dis_Alexi daily ET product. ET is a useful indicator for drought condition and plant consumptive use. Accurate measurements of ET are essential for water management and assessing the impacts of landcover on temperature regimes. Dis_Alexi uses the two source energy balance model (TSEB) to estimate ET from net radiation, soil heat conductance flux, sensible heat flux, and latent heat of vaporization: 
R_N-G=H+λE
In the TSEB model soil and canopy thermal radiances are considered as a linear sum and uses the fraction of vegetation cover at the thermal sensor view angle to separate the two. Instantaneous ET is converted to daily ET assuming a fixed relationship between solar radiation and ET throughout the day. The most significant factor in calculating ET in the dis_Alexi algorithm is land surface temperature (LST), which is measured by ECOSTRESS. An additional important factor in the algorithm is the Leaf Area Index (LAI), which is measured from Landsat 8. Temporal offsets between ECOSTRESS and Landsat data acquisition may cause errors in ET estimates if the land surface experiences changes between acquisitions (ie: harvest season or green-up). Additional data inputs from the climate forecasting system (CFSv2) include wind speed, air temperature, atmospheric pressure, and vapor pressure. Land cover inputs are obtained from the NLCD 30 m resolution data product. Despite frequent overpass time, several factors implicate the number of usable images including MODIS cloud cover and nighttime images gaps, which generally last about 20 days. In this study several steps were taken in order to accurate compare flux tower data to ECOSTRESS data including the following:

1.	ECOSTRESS observation time converted to local time.
2.	Eddy covariance measurements obtained for those days. 
3.	Eddy covariance measurements with recorded precipitation were removed.
4.	Eddo covariance measurements with latent heat fluxes less than -10 W/m2 were removed. 
5.	Closure correction applied to eddy covariance for the entire day.
6.	Linear interpolation of eddy covariance measurements to fill gaps.
7.	Outliers removed if they exceed 3 standard deviations. 
8.	The area under the LE curve is integrated to obtain daily ET measurements in W/m2 and multiplied by 0.03521 (assuming latent heat of vaporization at 20 deg C)

Results showed the importance of additional filtering of ECOSTRESS images based on the view zenith (VZ) angle and aerosol optical depth (AOD). Images acquired at under VZ angles greater than 20 deg should be removed from comparison as there is an increase in misregistration between Landsat inputs and ECOSTRESS. CONUS wide comparison produce and R2 = 0.80 and an RMSE = 0.81 mm/day. 



### Liang et al., 2022

**Citation:** *Liang, L., Feng, Y., Wu, J., He, X., Liang, S., Jiang, X., de Oliveira, G., Qiu, J. and Zeng, Z., 2022. Evaluation of ECOSTRESS evapotranspiration estimates over heterogeneous landscapes in the continental US. Journal of Hydrology, 613, p.128470.*

**DOI:** https://doi.org/10.1016/j.jhydrol.2022.128470

**Findings:** 
This study compares ECOSTRESS products disALEXI (Two Source Energy Balance model) and PT-JPL (Priestley-Taylor model) to eddy flux towers across various geographic regions and biome types. In general, disALEXI performed better and was able to capture values closer to in-situ ground measurements. However, PT-JPL was able to better capture differences among heterogeneous landscapes. Overall, geographic region and local climate had a greater influence on ET than biome types. ECOSTRESS products also tended to overestimate early morning ET while also observing peak ET values an hour later than in situ observations. Both products had poor R2 values for daily ET estimates (0.11 and 0.45 for PT-JPL and disALEXI respectively), however disALEXI preformed better in Arizona and Colorado. Additionally, both products were able to capture seasonal variability of ET that followed the in situ trends. When quality flags were applied to disALEXI data – only selecting quality bits equal to zero, as well as removing high VZ and AOD pixels – the R2 dramatically increased (from 0.53 to 0.8), but the number of data pairs was significantly reduced (from 409 to 90). The R squared value was much less than the Fischer study, which could be due to over representation in WI and higher number of data pairs. In general the quality of ECOSTRESS products was determined by geographic region and local climate, rather than vegetation type. The authors claim that ECOSTRESS is a good product for measuring field scale response in homogeneous landscapes (ie crop response to water stress) but less sufficient at mapping ET across heterogeneous, complex landscapes.

 **Additional Notes:**
- Previous work validating ECOSTRESS 
- Methods for correcting and filtering eddy flux data
- Methods used ET boundaries between 0 – 30 mm/day (removed the rest)
- Kohli et at 2020 foudnsite specific differences in ET product partly being to spatial heterogeniety near the site



### Nicholson et al., 2020

**Title:** *Sensitivity and uncertainty quantification for the ECOSTRESS evapotranspiration algorithm – DisALEXI. *

**Authors:** Cawse-Nicholson, K., Braverman, A., Kang, E. L., Li, M., Johnson, M., Halverson, G., Anderson, M., Hain, C., Gunson, M., & Hook, S. 

**Year:** 2020

**DOI:** https://doi.org/10.1016/j.jag.2020.102088

**Findings:** 
This study quantifies the uncertainty associated with the disALEXI ET product. It is important to understand the differences between validation (comparison with field data), verification (comparison with other models), and uncertainty quantification. This study defined uncertainty quantification as the variability of the output when all inputs are varied in a reasonable way. This study concluded that uncertainty of ECOSTRESS was higher than the observed in previous validation studies. The study also found that that land surface temperature (LST) obtained from ECOSTRESS was the main driver of uncertainty, followed by albedo and LAI provided by Landsat. 



### Anderson et al, 2021

**Citation:** *Martha C. Anderson, Yang Yang, Jie Xue, Kyle R. Knipper, Yun Yang, Feng Gao, Chris R. Hain, William P. Kustas, Kerry Cawse-Nicholson, Glynn Hulley, Joshua B. Fisher, Joseph G. Alfieri, Tilden P. Meyers, John Prueger, Dennis D. Baldocchi, Camilo Rey-Sanchez, 2021. Interoperability of ECOSTRESS and Landsat for mapping evapotranspiration time series at sub-field scales, Remote Sensing of Environment, Volume 252, 2021, 112189, ISSN 0034-4257.*

**DOI:** https://doi.org/10.1016/j.rse.2020.112189.

**Findings:** 

- Images should be filtered by < 20 degree viewing angle
- Used imaged between the hours of 9 am and 5 pm (constrains on image aquisition time)
- ECOSTRESS only slightly improve ET measurements, but significanlty improved at specific sites when it was able to capture peak growth stage
- Early morning image aquisition produced 'excessively' uniform ET maps


### Hu et al, 2023

**Citation:** *Hu, T., Mallick, K., Hitzelberger, P., Didry, Y., Boulet, G., Szantoi, Z., Koetz, B., Alonso, I., Pascolini‐Campbell, M., Halverson, G. and Cawse‐Nicholson, K., 2023. Evaluating European ECOSTRESS hub evapotranspiration products across a range of soil‐atmospheric aridity and biomes over Europe. Water Resources Research, 59(8), p.e2022WR034132.*

**DOI:** https://doi.org/10.1016/j.rse.2022.113296.

**Findings:**

- PT-JPL overestimated Et in shrub lands and savanas due to constraints from land surface temperature in the model
- There is an increase in ET bias with progressive surface drying
- SEBS model showed large over estimation under drying conditions
- SEBS could not capture low ET over shrubland and savanna
- All models over estimated ET in sparsely vegetated regions
- ET bias increases with VPD, which corresponds to dry conditions
- ET bias was effected by overpass time

**Additional Notes:**
- Coupling between the land surface and atmosphere are strong in water limited systems, ET is mainly driven by stomatal conductance (Mallick et al., 2016, 2022).



### Hulley et al, 2021

**Citation:** *Hulley, G. C., Göttsche, F. M., Rivera, G., Hook, S. J., Freepartner, R. J., Martin, M. A., ... & Johnson, W. R. (2021). Validation and quality assessment of the ECOSTRESS level-2 land surface temperature and emissivity product. IEEE Transactions on Geoscience and Remote Sensing, 60, 1-23.*

**DOI:** https://doi.org/10.1016/j.rse.2022.113296.

**Findings:** 

- The ECOSTRESS LST product demonstrated a high level of accuracy when compared to in situ measurements
- With proper calibration and validation, the ECOSTRESS LST data could provide reliable temperature readings across diverse land cover types



### Wen et al., 2022

**Citation:** *Wen, J., Fisher, J.B., Parazoo, N.C., Hu, L., Litvak, M.E. and Sun, Y., 2022. Resolve the clear‐sky continuous diurnal cycle of high‐resolution ECOSTRESS evapotranspiration and land surface temperature. Water Resources Research, 58(9), p.e2022WR032227.*

**DOI:**  https://doi.org/10.1029/2022WR032227

**Findings:** 
- Daily measurements derived from scaled instantaneous  with solar radiation which assume linear scaling
- Other biotic and abiotic processes (like stomatal closure) are not considered

**Additional Notes:**



### Velpuri et al., 2013

**Citation:** *Velpuri, N.M., Senay, G.B., Singh, R.K., Bohms, S. and Verdin, J.P., 2013. A comprehensive evaluation of two MODIS evapotranspiration products over the conterminous United States: Using point and gridded FLUXNET and water balance ET. Remote Sensing of Environment, 139, pp.35-49.*

**DOI:** https://doi.org/10.1016/j.rse.2013.07.013

**Findings:** 
- Uncertainty up to 50% at point scale
- Uncertainty up to 25% at basin scale
- Both datasets were accurate
- Accuracy varies depending on landcover type and climate zone
- Under/over estimate depending on site conditions
...
**Additional Notes:**



### Tang et al., 2015

**Citation:** *Tang, R., Shao, K., Li, Z.L., Wu, H., Tang, B.H., Zhou, G. and Zhang, L., 2015. Multiscale validation of the 8-day MOD16 evapotranspiration product using flux data collected in China. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 8(4), pp.1478-1486.*

**DOI:** 10.1109/JSTARS.2015.2420105

**Findings:**
- MOD16 reproduces temporal patterns
- Underestimate at high levels of ET and overestimate at low levels of ET
- Underestimate irrigated conditions
- Larger area has better agreement than smaller area extracted
- Agreement between sites is not consitent
  

**Additional Notes:**


### Volk et al., 2024

**Citation:** *Volk, J.M., Huntington, J.L., Melton, F.S., Allen, R., Anderson, M., Fisher, J.B., Kilic, A., Ruhoff, A., Senay, G.B., Minor, B. and Morton, C., 2024. Assessing the accuracy of OpenET satellite-based evapotranspiration data to support water resource and land management applications. Nature Water, 2(2), pp.193-205.*

**DOI:** https://doi.org/10.1038/s44221-023-00181-7

**Findings:** 
- Slight underestimation of ET in croplands
- High variability and lower accuracy at shrublands and forested sites
- Natural settings perform worse than agriultural ones
