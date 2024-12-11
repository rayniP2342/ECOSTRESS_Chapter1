# ECOSTRESS Literature Review

This document summarizes findings from various papers relating to ECOSTRESS.

# Nicholson et al 2021

**Title:** *Evaluation of a CONUS-Wide ECOSTRESS DisALEXI Evapotranspiration Product*

**Authors:** Cawse-Nicholson, K., Anderson, M. C., Yang, Y., Yang, Y., Hook, S. J., Fisher, J. B., Halverson, G., Hulley, G. C., Hain, C., Baldocchi, D. D., Brunsell, N. A., Desai, A. R., Griffis, T. J., & Novick, K. A. 

**Year:** 2021

**DOI:** https://doi.org/10.1109/JSTARS.2021.3111867

**Findings:** This study uses eddy flux tower data to validate the ECOSTRESS dis_Alexi daily ET product. ET is a useful indicator for drought condition and plant consumptive use. Accurate measurements of ET are essential for water management and assessing the impacts of landcover on temperature regimes. Dis_Alexi uses the two source energy balance model (TSEB) to estimate ET from net radiation, soil heat conductance flux, sensible heat flux, and latent heat of vaporization: 
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


