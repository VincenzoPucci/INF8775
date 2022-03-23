from tp import main



if __name__ == "__main__":
    time_list = []
    height_list = []
    full_example_size = [100, 500, 1000, 5000, 10000, 50000, 100000]
    for sz in [100]:
        t_avg = []
        h_avg = []
        for algo in ['glouton', 'progdyn', 'tabou']:
            h_tot = 0
            t_tot = 0
            for i in range(10):
                h, t = main(["-a", str(algo), "-e", f"b{sz}_{i+1}.txt"])
                h_tot += h
                t_tot += t
            t_avg.append(h_tot/10)
            h_avg.append(t_tot/10)
        time_list.append(t_avg)
        height_list.append(h_avg)

    print(time_list)
    print(height_list)
        