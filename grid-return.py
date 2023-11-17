def to_grid(dec_lat, dec_lon):
    if not (-180 <= dec_lon < 180) or not (-90 <= dec_lat < 90):
        sys.stderr.write('Invalid coordinates\n')
        sys.exit(1)

    adj_lat = dec_lat + 90.0
    adj_lon = dec_lon + 180.0

    grid_lat_sq = upper[int(adj_lat / 10)]
    grid_lon_sq = upper[int(adj_lon / 20)]

    grid_lat_field = str(int(adj_lat % 10))
    grid_lon_field = str(int((adj_lon / 2) % 10))

    adj_lat_remainder = (adj_lat - int(adj_lat)) * 60
    adj_lon_remainder = ((adj_lon) - int(adj_lon / 2) * 2) * 60

    grid_lat_subsq = lower[int(adj_lat_remainder / 2.5)]
    grid_lon_subsq = lower[int(adj_lon_remainder / 5)]

    return grid_lon_sq + grid_lat_sq + grid_lon_field + grid_lat_field + grid_lon_subsq + grid_lat_subsq
