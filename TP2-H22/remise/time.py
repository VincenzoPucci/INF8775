from tp import main



if __name__ == "__main__":
    time_list = []
    height_list = []
    length_list = []
    full_example_size = [100, 500, 1000, 5000, 10000, 50000, 100000]
    n_sample = 10
    for sz in full_example_size:
        t_avg = []
        h_avg = []
        l_avg = []
        for algo in ['glouton', 'progdyn', 'tabou']:
            h_tot = 0
            t_tot = 0
            l = 0
            for i in range(n_sample):
                res, h, t = main(["-a", str(algo), "-e", f"b{sz}_{i+1}.txt"])
                h_tot += h
                t_tot += t
                l += len(res)
            t_avg.append(h_tot/n_sample)
            h_avg.append(t_tot/n_sample)
            l_avg.append(l/n_sample)
        time_list.append(t_avg)
        height_list.append(h_avg)
        length_list.append(l_avg)
    
    print(time_list)
    print(height_list)
    print(length_list)
        