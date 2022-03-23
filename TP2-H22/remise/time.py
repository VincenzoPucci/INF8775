from tp import main



if __name__ == "__main__":
    time_list = []
    height_list = []
    h_tot = 0
    t_tot = 0
    for algo in ['glouton', 'progdyn', 'tabou']:
        for i in range(10):
            h, t = main(["-a", "glouton", "-e", f"b100_{i+1}.txt"])
            h_tot += h
            t_tot += t
        time_list.append(h_tot/10)
        height_list.append(t_tot/10)
    print(time_list)
    print(height_list)
        