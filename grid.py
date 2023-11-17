import sys

# Convert latitude and longitude to Maidenhead grid locators.
#
# Arguments are in signed decimal latitude and longitude. For example,
# the location of my QTH Palo Alto, CA is: 37.429167, -122.138056 or
# in degrees, minutes, and seconds: 37° 24' 49" N 122° 6' 26" W

upper = 'ABCDEFGHIJKLMNOPQRSTUVWX'
lower = 'abcdefghijklmnopqrstuvwx'

def to_grid(dec_lat, dec_lon):
    if not (-180 <= dec_lon < 180):
        sys.stderr.write('longitude must be -180<=lon<180, given %f\n' % dec_lon)
        sys.exit(32)
    if not (-90 <= dec_lat < 90):
        sys.stderr.write('latitude must be -90<=lat<90, given %f\n' % dec_lat)
        sys.exit(33)  # can't handle north pole, sorry, [A-R]

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

def usage():
    print('This script takes two arguments, decimal latitude and longitude.')
    print('Example for Newington, Connecticut (W1AW):')
    print('python maidenhead.py 41.714775 -72.727260')
    print('returns: FN31pr')

def test():
    # First four test examples are from "Conversion Between Geodetic and Grid Locator Systems",
    # by Edmund T. Tyson N5JTY QST January 1989
    test_data = (
        ('Munich', (48.14666, 11.60833), 'JN58td'),
        ('Montevideo', (-34.91, -56.21166), 'GF15vc'),
        ('Washington, DC', (38.92, -77.065), 'FM18lw'),
        ('Wellington', (-41.28333, 174.745), 'RE78ir'),
        ('Newington, CT (W1AW)', (41.714775, -72.727260), 'FN31pr'),
        ('Palo Alto (K6WRU)', (37.413708, -122.1073236), 'CM87wj'),
    )
    print('Running self-test\n')
    passed = True
    for name, latlon, grid in test_data:
        print('Testing %s at %f %f:' % (name, latlon[0], latlon[1]))
        test_grid = to_grid(latlon[0], latlon[1])
        if test_grid != grid:
            print('Failed ' + test_grid + ' should be ' + grid)
            passed = False
        else:
            print('Passed ' + test_grid)
    print('')
    if passed:
        print('Passed!')
    else:
        print('Failed!')

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        usage()
        print('')
        test()
    else:
        print(to_grid(float(argv[1]), float(argv[2])))

if __name__ == "__main__":
    main()
