import xarray as xr
from cartopy.util import add_cyclic_point

def lon_to_360(dlon: float) -> float:
  return ((360 + (dlon % 360)) % 360)

def roll_longitude(ds,londim='longitude'):
    return ds.assign_coords(longitude=(((ds.longitude + 180) % 360) - 180)).sortby(londim)

#source: https://gist.github.com/brews/95e167fb7df997864304f07ee321f4fd
def cyclic_wrapper(x, dim="lon"):
    """So add_cyclic_point() works on 'dim' via xarray Dataset.map()"""
    wrap_data, wrap_lon = add_cyclic_point(
        x.values, 
        coord=x.coords[dim].data,
        axis=x.dims.index(dim)
    )
    return xr.DataArray(
        wrap_data, 
        coords={dim: wrap_lon, **x.drop(dim).coords}, 
        dims=x.dims
    )
