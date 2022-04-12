from tp import main

def write_results(path, results, sz):
    with open(path, "a") as f:
        f.write(f"sample_size: {sz} \n")
        for r in results:
            f.write(str(r) + str("\n"))
        f.write(str("\n"))
    return


if __name__ == "__main__":

    file_path = "full_results.txt"

    time_avg_list = []
    height_avg_list = []
    length_avg_list = []
    full_example_size = [10000, 50000, 100000]
    n_sample = 10
    for sz in full_example_size:
        print(f"n= {sz}")
        t_avg = []
        h_avg = []
        l_avg = []

        time_list = []
        height_list = []

        for algo in ['glouton', 'progdyn', 'tabou']:
            h_list = []
            t_list = []
            print(f"algo: {algo}")
            h_tot = 0
            t_tot = 0
            l = 0
            for i in range(n_sample):
                res, h, t = main(["-a", str(algo), "-e", f"b{sz}_{i+1}.txt"])
                h_tot += h
                t_tot += t
                l += len(res)
                h_list.append(h)
                t_list.append(t)
        
            t_avg.append(h_tot/n_sample)
            h_avg.append(t_tot/n_sample)
            l_avg.append(l/n_sample)

            time_list.append(t_list)
            height_list.append(h_list)


        write_results(file_path, [time_list, height_list, t_avg, h_avg, l_avg], sz)

        time_avg_list.append(t_avg)
        height_avg_list.append(h_avg)
        length_avg_list.append(l_avg)
    
    print("Finish !")
        