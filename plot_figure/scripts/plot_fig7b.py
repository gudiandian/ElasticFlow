import matplotlib.pyplot as plt
import csv

submit_filename = "../ElasticFlow/traces_for_ElasticFlow/195job_endtoebd_trace.csv"
experi_filename = "../logs/figure6b/ef-accessctrl/job.csv"
output_filename = "fig7b.pdf"
step = 10 # step minutes
scale = 60 // step;
fontsizeValue=28

def hist_gen(filename):
    submission_time = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            submission_time.append(int(line['submit_time']))
    submission_time = [(t - submission_time[0]) // 60 // step for t in submission_time]
    hist = dict.fromkeys(range(48 * scale), 0)
    for t in submission_time:
        hist[t] += 1
    print(hist)
    return hist

submit_hist = hist_gen(submit_filename)
experi_hist = hist_gen(experi_filename)
plt.figure(figsize=(20, 7))
plt.xlim(0, 48 * scale)
plt.ylim(0, 25)
plt.grid(True, color="#D3D3D3")
labels = ["# job submission", "# job accepted in cluster experiment"]
p_submit = plt.plot(submit_hist.keys(), submit_hist.values(), label="# job submission", linewidth=3, color="r")
p_experi = plt.plot(experi_hist.keys(), experi_hist.values(), ":", label="# job accepted in cluster experiment", linewidth=3, color="b")
plt.xlabel("Time (hour)", fontsize=fontsizeValue)
plt.ylabel("Number of Jobs", fontsize=fontsizeValue)
plt.xticks([0, 12 * scale, 24 * scale, 36 * scale, 48 * scale], [0, 12, 24, 36, 48])
plt.tick_params(axis='both', which='major', labelsize=fontsizeValue)
plt.tick_params(bottom=False, top=False, left=False, right=False)
plt.legend(fontsize=fontsizeValue)
plt.savefig(output_filename)
