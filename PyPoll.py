import os
import csv

output_file = 'election_summary.txt'

csv_input_path = os.path.join("Resources", "election_data.csv")
txt_output_path = os.path.join("Resources", output_file)
candidates, total_candidates, candidate_perc, candidate_total, summaries = ([] for i in range(5))
with open(csv_input_path, mode='r', newline='') as poll_data:
  reader = csv.reader(poll_data, delimiter=',')
  next(reader)
  num_rows = 0
  for row in reader:
    total_candidates.append(row[2])
    num_rows += 1

sorted_candidates = sorted(total_candidates)
for i in range(num_rows):
  if sorted_candidates[i - 1] != sorted_candidates[i]:
    candidates.append(sorted_candidates[i])

print("Election Results")
print("-" * 30)
print("Total Votes:", num_rows)
print("-" * 30)
for j in range(len(candidates)):
  candidate_count = 0
  for k in range(len(sorted_candidates)):
    if candidates[j] == sorted_candidates[k]:
      candidate_count += 1
  candidate_perc.append(round(candidate_count / num_rows * 100, 1))
  candidate_total.append(candidate_count)
candidate_zip = zip(candidates, candidate_perc, candidate_total)
for row in candidate_zip:
  print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
  summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
  summaries.append(summary)
for k in range(len(candidate_perc)):
  if candidate_total[k] > candidate_total[k - 1]:
    name_winner = candidates[k]
print("-" * 30)
print("Winner:", name_winner)
print("-" * 30)
with open(txt_output_path, mode='w', newline='') as posted_summaries:
  writer = csv.writer(posted_summaries)
  writer.writerows([
    ["Election Results for: "],
    ["-" * 30],
    ["Total Votes: " + str(num_rows)],
    ["-" * 30]
  ])
  writer.writerows(summaries)
  writer.writerows([
    ["-" * 30],
    ["Winner: " + str(name_winner)],
    ["-" * 30]
  ])