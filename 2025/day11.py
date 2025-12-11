import time



def main():
    with open("input/day11.txt", "r") as file:
        file_content = file.read().splitlines()

    cache = {}
    servers = {}
    for line in file_content:
        split = line.split()
        servers[split[0].strip(":")] = split[1:]

    # print(servers)

    complete_paths = count_paths('you', 'out', servers, cache)
    print(complete_paths)

    start_to_fft = count_paths('svr', 'fft', servers, cache)
    start_to_dac = count_paths('svr', 'dac', servers, cache)
    dac_to_fft = count_paths('dac', 'fft', servers, cache)
    fft_to_dac = count_paths('fft', 'dac', servers, cache)
    fft_to_out = count_paths('fft', 'out', servers, cache)
    dac_to_out = count_paths('dac', 'out', servers, cache)

    paths_through_fft_first = start_to_fft * fft_to_dac * dac_to_out
    paths_through_dac_first = start_to_dac * dac_to_fft * fft_to_out
    total_paths = paths_through_fft_first + paths_through_dac_first
    print(total_paths)


def count_paths(start: str, end: str, servers: dict[str, str], cache: dict[tuple[str, str], int]) -> int:
    if (start, end) in cache:
        return cache[(start, end)]

    if start == end:
        return 1

    total_paths = 0
    if start in servers:
        for neighbor in servers[start]:
            total_paths += count_paths(neighbor, end, servers, cache)

    cache[(start, end)] = total_paths
    return total_paths


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Executed in: %s seconds." % (time.time() - start_time))