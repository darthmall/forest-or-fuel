# Forest or Fuel

Reproduce the analysis from [_Assessing the comparative productivity advantage of bioenergy feedstocks at different latitudes_](https://doi.org/10.1088/1748-9326/7/4/045906).

## Set up

You'll need to install [Pipenv](https://docs.pipenv.org/) first. Then:

    $ pipenv install
    $ pipenv run jupyter lab

## Get the Data

You'll need the NetCDF files for the following datasets to run these notebooks.

### EarthStat

Download the _Harvested Area and Yield for 175 Crops_ and _Potential Natural Vegetation_ dataset from [earthstat.org/data-download](http://www.earthstat.org/data-download/). Place the yield data in `data/crops` and the vegetation data in `data/biomes`.

### Climatic Research Unit Time-Series v4.01

Download the full temperature (`tmp`) and precipitation (`pre`) data (1901–2016) from the (Centre for Environmental Data Analysis)[http://catalogue.ceda.ac.uk/uuid/58a8802721c94c66ae45c3baa4d814d0]. You'll need to register for an account. Place the `.nc` files directly in `data`.
