import sys

def process_all(lines):
    seed_ranges = list(int(x) for x in lines[0].split(':')[1].split())

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    current_map = seed_to_soil

    for line in lines[2:]:
        if line.startswith('seed-to-soil'):
            current_map = seed_to_soil
            continue
        if line.startswith('soil-to-fertilizer'):
            current_map = soil_to_fertilizer
            continue
        if line.startswith('fertilizer-to-water'):
            current_map = fertilizer_to_water
            continue
        if line.startswith('water-to-light'):
            current_map = water_to_light
            continue
        if line.startswith('light-to-temperature'):
            current_map = light_to_temperature
            continue
        if line.startswith('temperature-to-humidity'):
            current_map = temperature_to_humidity
            continue
        if line.startswith('humidity-to-location'):
            current_map = humidity_to_location
            continue

        conversion = [int(x) for x in line.split()]
        if conversion:
            current_map.append(conversion)

    def sort_mapping(mapping):
        return list(sorted(mapping, key=lambda c: c[1]))

    seed_to_soil = sort_mapping(seed_to_soil)
    soil_to_fertilizer = sort_mapping(soil_to_fertilizer)
    fertilizer_to_water = sort_mapping(fertilizer_to_water)
    water_to_light = sort_mapping(water_to_light)
    light_to_temperature = sort_mapping(light_to_temperature)
    temperature_to_humidity = sort_mapping(temperature_to_humidity)
    humidity_to_location = sort_mapping(humidity_to_location)
    def get_mapping_range(mapping, range):
        print('range', range)
        [start, length] = range
        for [dest_start, src_start, mapping_length] in mapping:
            c = [dest_start, src_start, mapping_length]
            while length > 0:
                if start + length < src_start: # way before
                    print('case 1', start, length, c)
                    yield [start, length]
                    length = 0
                    break
                elif start >= src_start + mapping_length: # way after
                    # print('case 2', start, length, c)
                    break
                elif start < src_start <= start + length: # we have a small range before
                    print('case 3', start, length, c)
                    used_length = src_start - start
                    remaining_length = length - used_length
                    yield [start, used_length]

                    start = src_start
                    length = remaining_length
                elif src_start <= start < src_start + mapping_length: # we have a part inside
                    print('case 4', start, length, c)
                    end = min(src_start + mapping_length, start + length)
                    used_length = end - start
                    remaining_length = length - used_length
                    yield [dest_start + start - src_start, used_length]

                    start = end
                    length = remaining_length
                elif src_start <= start <= src_start + mapping_length < start + length: # we have an extra piece after
                    print('case 5', start, length, c)
                    used_length = start - src_start
                    remaining_length = length - used_length
                    yield [dest_start + start - src_start, used_length]

                    start = src_start + mapping_length
                    length = remaining_length
                else:
                    print('case UKNOWN', start, length, c)
                    raise OSError()

        if length > 0:
            print('case 6', start, length, c)
            yield [start, length]

    def get_seed_ranges():
        for i in range(len(seed_ranges) // 2):
            yield [seed_ranges[2 * i], seed_ranges[2 * i + 1]]

    def flatten(iterable):
        not_sorted = [item for row in iterable for item in row]
        ls = list(sorted(not_sorted, key=lambda x: x[0]))
        print('not sorted', not_sorted)
        print('result', ls)
        print()
        return ls

    soil_ranges = flatten(get_mapping_range(seed_to_soil, range) for range in get_seed_ranges())
    fertilizer_ranges = flatten(get_mapping_range(soil_to_fertilizer, range) for range in soil_ranges)
    water_ranges = flatten(get_mapping_range(fertilizer_to_water, range) for range in fertilizer_ranges)
    light_ranges = flatten(get_mapping_range(water_to_light, range) for range in water_ranges)
    temperature_ranges = flatten(get_mapping_range(light_to_temperature, range) for range in light_ranges)
    humidity_ranges = flatten(get_mapping_range(temperature_to_humidity, range) for range in temperature_ranges)
    location_ranges = flatten(get_mapping_range(humidity_to_location, range) for range in humidity_ranges)

    print()
    print(soil_ranges)
    print(fertilizer_ranges)
    print(water_ranges)
    print(light_ranges)
    print(temperature_ranges)
    print(humidity_ranges)
    print('location', location_ranges)

    # return 0
    return min(location_ranges, key=lambda r: r[0])[0]

if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
