import matplotlib.pyplot as plt
import csv

edf_file = "../logs/figure6b/edf/scheduling_events.csv"
elasticflow_file = "../logs/figure6b/ef-accessctrl/scheduling_events.csv"
g_file = "../logs/figure6b/gandiva/scheduling_events.csv"
t_file = "../logs/figure6b/dlas-gpu/scheduling_events.csv"
themis_file = "../logs/figure6b/themis/scheduling_events.csv"
chronus_file = "../logs/figure6b/chronus/scheduling_events.csv"
step = 5 # step minutes
scale = 60 // step;
fontsizeValue=28

def hist_gen(filename):
    submission_time = []
    gpu_allocation = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            submit_time = int(line['time'])
            submission_time.append(submit_time)
            gpu_num = 0
            for k, v in line.items():
                if k and "gpu" in k and v != "":
                    gpu_num += 1
            gpu_allocation.append(gpu_num)
    submission_time = [(t - submission_time[0]) / 60 / step for t in submission_time]
    return {k: v for k, v in zip(submission_time, gpu_allocation)}


def chronus_hist_gen(filename):
    submission_time = []
    gpu_allocation = []
    last_time = -1210
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            submit_time = int(line['time'])
            if submit_time - last_time < 1200:
                continue
            last_time = submit_time
            submission_time.append(submit_time)
            gpu_num = int(line['full_resource']) - int(line['free_resource'])
            gpu_allocation.append(gpu_num)
    submission_time = [(t - submission_time[0]) / 60 / step for t in submission_time]
    return {k: v for k, v in zip(submission_time, gpu_allocation)}

gandiva = hist_gen(g_file)
tiresias_L = hist_gen(t_file)
elasticflow = hist_gen(elasticflow_file)
themis = hist_gen(themis_file)
edf = hist_gen(edf_file)
chronus = chronus_hist_gen(chronus_file)

plt.figure(figsize=(20, 7))
plt.xlim(0, 48 * scale)
plt.ylim(0, 140)
plt.grid(True, color="#D3D3D3")
plt.plot(edf.keys(), edf.values(), label='EDF',linewidth=3)
plt.plot(gandiva.keys(), gandiva.values(), ":", label='Gandiva',linewidth=3)
plt.plot(tiresias_L.keys(), tiresias_L.values(), "--", label='Tiresias',linewidth=3)
plt.plot(themis.keys(), themis.values(), "-.", label='Themis',linewidth=3)
plt.plot(chronus.keys(), chronus.values(), "--", label='Chronus',linewidth=3)
plt.plot(elasticflow.keys(), elasticflow.values(), "-.", label='ElasticFlow',linewidth=3)
plt.xticks([0, 12 * scale, 24 * scale, 36 * scale, 48 * scale], [0, 12, 24, 36, 48])
plt.yticks([0, 20, 40, 60, 80, 100, 120, 128])
plt.tick_params(axis='both', which='major', labelsize=fontsizeValue)
plt.tick_params(bottom=False, top=False, left=False, right=False)
plt.xlabel("Time (hour)", fontsize=fontsizeValue)
plt.ylabel("Number of allocated GPUs", fontsize=fontsizeValue)
plt.legend(fontsize=fontsizeValue, ncol=3)
plt.savefig("fig7a.pdf")