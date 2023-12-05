import sys

def process_all(lines):
    seeds = list(int(x) for x in lines[0].split(':')[1].split())

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

    def get_mapping(mapping, src):
        for conversion in mapping:
            [dest_start, src_start, length] = conversion
            if src_start <= src < src_start + length:
                return dest_start + src - src_start

        return src

    locations = []
    for seed in seeds:
        soil = get_mapping(seed_to_soil, seed)
        fertilizer = get_mapping(soil_to_fertilizer, soil)
        water = get_mapping(fertilizer_to_water, fertilizer)
        light = get_mapping(water_to_light, water)
        temperature = get_mapping(light_to_temperature, light)
        humidity = get_mapping(temperature_to_humidity, temperature)
        location = get_mapping(humidity_to_location, humidity)

        print(seed, soil, fertilizer, water, light, temperature, humidity, location)
        locations.append(location)

    print(locations)
    return min(locations)


if __name__ == '__main__':
    lines = list(sys.stdin.read().splitlines())

    result = process_all(lines)
    print(result)
